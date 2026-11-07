"""Regression checks in disposable copies; preserved evidence is never edited."""
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class EvidenceIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.project = pathlib.Path(self.tmp.name) / 'project'
        shutil.copytree(ROOT, self.project, ignore=shutil.ignore_patterns('.git', 'raw', 'results', 'figures', '__pycache__'))
        (self.project / 'raw').symlink_to(ROOT / 'raw', target_is_directory=True)
        self.manifest = self.project / 'evidencias/2026-11-07/SHA256SUMS'

    def fails_before_outputs(self, message):
        run = subprocess.run([sys.executable, str(self.project / 'scripts/reproduce.py')], capture_output=True, text=True)
        self.assertNotEqual(run.returncode, 0, run.stdout)
        self.assertIn(message, run.stderr)
        self.assertFalse((self.project / 'results').exists())

    def test_missing_manifest(self):
        self.manifest.unlink()
        self.fails_before_outputs('Manifesto de evidências ausente')

    def test_empty_manifest(self):
        self.manifest.write_text('# nenhuma entrada\n')
        self.fails_before_outputs('Manifesto de evidências vazio')

    def test_changed_evidence(self):
        _, relative = self.manifest.read_text().splitlines()[0].split(None, 1)
        target = self.manifest.parent / relative.strip().lstrip('*')
        target.write_bytes(target.read_bytes() + b'\nchanged\n')
        self.fails_before_outputs('Hash da evidência diverge')

if __name__ == '__main__':
    unittest.main()
