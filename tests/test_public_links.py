"""Denied hosts must be blocked without being requested or counted verified."""
import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('audit_public_links', ROOT / 'scripts/audit_public_links.py')
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class DeniedLinkTests(unittest.TestCase):
    def test_denied_status_never_verified(self):
        for status in (401, 403, 'BLOCKED', 0, 404):
            self.assertFalse(audit.external_status_verified(status))
        self.assertTrue(audit.external_status_verified(200))

    def test_skip_host_is_bounded_and_covers_subdomains(self):
        self.assertTrue(audit.host_is_skipped('https://evolink.ai/model', ['evolink.ai']))
        self.assertTrue(audit.host_is_skipped('https://www.evolink.ai/model', ['evolink.ai']))
        self.assertFalse(audit.host_is_skipped('https://not-evolink.ai/model', ['evolink.ai']))

    def test_skipped_host_never_requested_and_returns_failure(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            readme = root / 'README.md'
            readme.write_text('[Model](https://evolink.ai/gemini-4-hydrogen)\n')
            report = root / 'audit.md'
            with patch.object(audit, 'ROOT', root), patch.object(audit, 'public_files', return_value=[readme]), patch.object(audit, 'current_head', return_value='fixture'), patch.object(audit, 'check_external') as request, patch('sys.argv', ['audit', '--report', str(report), '--skip-host', 'evolink.ai']), contextlib.redirect_stdout(io.StringIO()):
                result = audit.main()
            request.assert_not_called()
            self.assertEqual(result, 1)
            self.assertIn('BLOCKED', report.read_text())
            self.assertIn('External URLs checked: 0', report.read_text())


class MethodEndpointDuplicateTests(unittest.TestCase):
    def test_only_required_reference_and_request_are_exempt(self):
        url = next(iter(audit.METHOD_BOUND_ENDPOINTS))
        text = f'`POST {url}`\n```bash\ncurl --request POST --url "{url}"\n```\n'
        self.assertTrue(audit.expected_method_endpoint_reuse('README.md', url, 2, text))
        for path, endpoint, count, body in [
            ('docs/api.md', url, 2, text),
            ('README.md', 'https://example.com', 2, text),
            ('README.md', url, 3, text),
            ('README.md', url, 2, text.replace('--request POST', '--request GET')),
            ('README.md', url, 2, text.replace('`POST ', '`GET ')),
        ]:
            self.assertFalse(audit.expected_method_endpoint_reuse(path, endpoint, count, body))
