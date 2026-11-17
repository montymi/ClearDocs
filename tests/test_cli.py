import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from click.testing import CliRunner
from cleardocs.cli import main


class CliTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.runner = CliRunner()

    def test_standard_site_builds(self):
        (self.root / 'README.md').write_text('# Original project\n', encoding='utf-8')
        result = self.runner.invoke(main, ['init', str(self.root), '--hosting', 'github-pages', '--site-name', 'A: "site"'])
        self.assertEqual(result.exit_code, 0, result.output)
        self.assertEqual((self.root / 'docs/index.md').read_text(), '# Original project\n')
        result = self.runner.invoke(main, ['build', '-f', str(self.root / 'mkdocs.yml')])
        self.assertEqual(result.exit_code, 0, result.output)
        self.assertIn('Original project', (self.root / 'site/index.html').read_text())
        workflow = (self.root / '.github/workflows/docs.yml').read_text()
        self.assertIn('actions/deploy-pages@v4', workflow)
        self.assertIn("github.event_name != 'pull_request'", workflow)

    def test_collision_is_atomic(self):
        (self.root / 'mkdocs.yml').write_text('existing')
        result = self.runner.invoke(main, ['init', str(self.root)])
        self.assertNotEqual(result.exit_code, 0)
        self.assertFalse((self.root / 'docs').exists())
        self.assertFalse((self.root / 'requirements-docs.txt').exists())
        self.assertEqual((self.root / 'mkdocs.yml').read_text(), 'existing')

    def test_minimal_and_readme_protection(self):
        result = self.runner.invoke(main, ['readme', str(self.root), '--name', 'Demo', '--description', 'Useful tool'])
        self.assertEqual(result.exit_code, 0, result.output)
        original = (self.root / 'README.md').read_text()
        self.assertIn('Useful tool', original)
        self.assertNotEqual(self.runner.invoke(main, ['readme', str(self.root)]).exit_code, 0)
        self.assertEqual((self.root / 'README.md').read_text(), original)
        result = self.runner.invoke(main, ['init', str(self.root), '--template', 'minimal'])
        self.assertEqual(result.exit_code, 0, result.output)
        self.assertFalse((self.root / 'docs/contributing.md').exists())
        self.assertFalse((self.root / '.github').exists())

    def test_symlink_destination_rejected(self):
        outside = self.root / 'outside'
        outside.mkdir()
        (self.root / 'docs').symlink_to(outside, target_is_directory=True)
        result = self.runner.invoke(main, ['init', str(self.root), '--force'])
        self.assertNotEqual(result.exit_code, 0)
        self.assertEqual(list(outside.iterdir()), [])

    def test_mkdocs_failure_propagates(self):
        config = self.root / 'mkdocs.yml'
        config.write_text('site_name: Broken\nnav:\n  - Missing: missing.md\n')
        (self.root / 'docs').mkdir()
        (self.root / 'docs/index.md').write_text('# Home')
        result = self.runner.invoke(main, ['build', '-f', str(config)])
        self.assertNotEqual(result.exit_code, 0)

    def test_serve_arguments(self):
        config = self.root / 'mkdocs.yml'
        config.write_text('site_name: Demo')
        with patch('cleardocs.cli.subprocess.run') as run:
            run.return_value.returncode = 0
            result = self.runner.invoke(main, ['serve', '-f', str(config), '--dev-addr', '127.0.0.1:8123'])
        self.assertEqual(result.exit_code, 0, result.output)
        self.assertEqual(run.call_args.args[0][-2:], ['--dev-addr', '127.0.0.1:8123'])


if __name__ == '__main__':
    unittest.main()
