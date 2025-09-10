import unittest
from pathlib import Path
import shutil
import os
from recursive_sort import recursive_sort
import tempfile

class TestFileCopying(unittest.TestCase):

    def setUp(self):
        # Створюємо тимчасові директорії
        self.test_dir = tempfile.TemporaryDirectory()
        self.src = Path(self.test_dir.name) / "src"
        self.dest = Path(self.test_dir.name) / "dest"
        self.src.mkdir()
        self.dest.mkdir()

        # Створюємо тестові файли
        (self.src / "file1.txt").write_text("text file")
        (self.src / "file2.jpg").write_text("image file")
        nested = self.src / "nested"
        nested.mkdir()
        (nested / "file3.txt").write_text("nested text")
        (self.src / "noextfile").write_text("no extension")

    def tearDown(self):
        # Очищення після тестів
        self.test_dir.cleanup()

    def test_copy_and_sort(self):
        recursive_sort(self.src, self.dest)

        self.assertTrue((self.dest / "txt" / "file1.txt").exists())
        self.assertTrue((self.dest / "jpg" / "file2.jpg").exists())
        self.assertTrue((self.dest / "txt" / "file3.txt").exists())
        self.assertTrue((self.dest / "no_extension" / "noextfile").exists())

    def test_empty_source(self):
        empty_src = self.src / "empty"
        empty_src.mkdir()
        recursive_sort(empty_src, self.dest)
        self.assertEqual(list(self.dest.iterdir()), [])

    @unittest.skipIf(os.name == 'nt', "Permissions semantics differ on Windows")
    def test_permission_error(self):
        restricted = self.src / "secret.txt"
        restricted.write_text("hidden")
        restricted.chmod(0)  # Забороняємо читання

        try:
            recursive_sort(self.src, self.dest)
        finally:
            restricted.chmod(0o644)  # Відновлюємо доступ

        self.assertFalse((self.dest / "txt" / "secret.txt").exists())

if __name__ == '__main__':
    unittest.main()