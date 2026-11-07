"""Regression checks in disposable copies; preserved evidence is never edited."""
import hashlib
import json
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
        # Exercise the real entry point with tiny, valid inputs. These checks
        # stop before analysis; the full dataset belongs to reproduction tests.
        for folder in ('scripts', 'raw', 'data', 'evidencias/2026-11-07'):
            (self.project / folder).mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / 'scripts/reproduce.py', self.project / 'scripts/reproduce.py')
        snapshot = self.project / 'raw/fixture.txt'
        snapshot.write_bytes(b'snapshot fixture\n')
        (self.project / 'data/snapshot-manifest.json').write_text(json.dumps([
            {'file': 'raw/fixture.txt', 'sha256': hashlib.sha256(snapshot.read_bytes()).hexdigest()}
        ]))
        self.manifest = self.project / 'evidencias/2026-11-07/SHA256SUMS'
        evidence = self.manifest.parent / 'fixture.txt'
        evidence.write_bytes(b'evidence fixture\n')
        digest = hashlib.sha256(evidence.read_bytes()).hexdigest()
        self.manifest.write_text(f'\n# Test evidence manifest\n{digest}  fixture.txt\n')

    def fails_before_outputs(self, message):
        run = subprocess.run([sys.executable, str(self.project / 'scripts/reproduce.py')], capture_output=True, text=True)
        self.assertNotEqual(run.returncode, 0, run.stdout)
        self.assertIn(message, run.stderr)
        self.assertFalse((self.project / 'results').exists())
        self.assertFalse((self.project / 'figures').exists())

    def test_missing_manifest(self):
        self.manifest.unlink()
        self.fails_before_outputs('Manifesto de evidências ausente')

    def test_empty_manifest(self):
        self.manifest.write_text('# nenhuma entrada\n')
        self.fails_before_outputs('Manifesto de evidências vazio')

    def test_changed_evidence(self):
        entry = next(line for line in self.manifest.read_text().splitlines()
                     if line.strip() and not line.startswith('#'))
        _, relative = entry.split(None, 1)
        target = self.manifest.parent / relative.strip().lstrip('*')
        target.write_bytes(target.read_bytes() + b'\nchanged\n')
        self.fails_before_outputs('Hash da evidência diverge')

if __name__ == '__main__':
    unittest.main()
