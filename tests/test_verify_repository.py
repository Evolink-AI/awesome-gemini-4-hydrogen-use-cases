"""Mutation regressions against the independently frozen source inventory."""
import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('verify_repository', ROOT / 'scripts/verify_repository.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class ValidationMutations(unittest.TestCase):
    def setUp(self):
        self.inventory = json.loads((ROOT / 'data/source-inventory.json').read_text())
        self.data = {'selected_case_count': self.inventory['selected_count'], 'items': []}
        for c in self.inventory['cases']:
            item = {k: c[k] for k in ('public_number', 'candidate_id', 'source_url', 'author_handle', 'author_url', 'date', 'category_key', 'prompt_public', 'prompt_text')}
            item['id'] = c['source_post_id']
            item['media_source_urls'] = [a['source_url'] for a in c['source_media']]
            item['media_assets'] = [dict(kind=a['kind'], source_url=a['source_url'], url=v.R2_PREFIX + str(c['public_number']) + ('.mp4' if a['kind'] == 'video' else '.jpg'), poster_url=v.R2_PREFIX + str(c['public_number']) + '-poster.jpg') for a in c['source_media']]
            self.data['items'].append(item)
        self.data['category_order'] = list(dict.fromkeys(c['category_key'] for c in self.inventory['cases']))
        self.data['category_names'] = {k:k for k in self.data['category_order']}

    def test_independent_inventory_valid_fixture(self):
        self.assertEqual(v.validate_source_inventory(self.data, self.inventory), [])

    def test_source_identity_mutations(self):
        for field in ('source_url', 'date', 'author_handle', 'id', 'category_key'):
            with self.subTest(field=field):
                data = copy.deepcopy(self.data)
                data['items'][0][field] = 'wrong'
                self.assertTrue(v.validate_source_inventory(data, self.inventory))

    def test_removed_or_replaced_source_media_fails(self):
        for mutation in ('remove', 'replace', 'poster'):
            data = copy.deepcopy(self.data)
            assets = data['items'][0]['media_assets']
            if mutation == 'remove':
                assets.clear()
            elif mutation == 'replace':
                assets[0]['source_url'] = 'https://example.com/unrelated.mp4'
            else:
                assets[0]['poster_url'] = ''
            self.assertTrue(v.validate_source_inventory(data, self.inventory))

    def test_truncating_both_canonical_counts_does_not_pass(self):
        self.data['items'].pop()
        self.data['selected_case_count'] -= 1
        self.assertTrue(v.validate_source_inventory(self.data, self.inventory))

    def test_utm_mutation(self):
        valid = v.MODEL_PAGE + '?utm_source=github&utm_medium=banner&utm_campaign=' + v.CAMPAIGN + '&utm_content=readme_banner'
        self.assertEqual(v.validate_conversion_url(valid, 'README.md'), [])
        self.assertTrue(v.validate_conversion_url(valid.replace('utm_source=github', 'utm_source=other'), 'README.md'))
        self.assertTrue(v.validate_conversion_url(v.MODEL_PAGE, 'README.md'))

    def test_localization_copy_fails(self):
        item = dict(public_number=1, title='Title', takeaway='Takeaway', body_notes='Notes')
        self.assertTrue(v.validate_localized_case(dict(title='Title', takeaway='Takeaway', notes='Notes'), item, 'es'))
        self.assertEqual(v.validate_localized_case(dict(title='Título', takeaway='Conclusión', notes='Notas'), item, 'es'), [])

    def test_disclaimer_is_not_smoke_claim(self):
        self.assertEqual(v.validate_public_copy("The reported build time is not independently verified.", "README.md"), [])
        self.assertTrue(v.validate_public_copy("Independently verified smoke test passed.", "README.md"))

    def test_stale_model_and_endpoint_tracking_fail(self):
        self.assertTrue(v.validate_public_copy('Gemini 3.6 Flash', 'README.md'))
        self.assertTrue(v.validate_public_copy('https://direct.evolink.ai/v1beta/models/gemini-4-hydrogen:generateContent?utm_source=github', 'README.md'))
        self.assertEqual(v.validate_public_copy('https://github.com/Evolink-AI/awesome-gemini-3.6-flash-guide-and-use-cases', 'README.md'), [])

class ConversionPlacementMutations(unittest.TestCase):
    def test_exact_eight_roles_and_wrong_placement(self):
        placements = [
            ('banner', 'readme_banner'), ('badge', 'model_try'),
            ('badge', 'model_for_docs'), ('readme', 'landing_overview'),
            ('overview', 'model_for_api_key'), ('quickstart', 'browser_try'),
            ('quickstart', 'model_for_api_key'), ('quickstart', 'model_for_docs'),
        ]
        actual = {v.MODEL_PAGE: placements}
        self.assertEqual(v.validate_conversion_placements(actual, 'README.md'), [])
        placements[-1] = ('quickstart', 'model_link')
        self.assertTrue(v.validate_conversion_placements(actual, 'README.md'))


if __name__ == '__main__':
    unittest.main()
