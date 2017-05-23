"""Analysis checks for the output of the pybytecompile script
"""

import unittest
from pathlib import Path

from bin import pybytecompiler


class TestCompileOutput(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.source_file_path = Path(pybytecompiler.__file__)
        self.source_file_compiled = self.source_file_path.parent.joinpath(
            ".".join([self.source_file_path.stem, "pyc"])
        )

    def tearDown(self):
        super().tearDown()
        if self.source_file_compiled.exists():
            self.source_file_compiled.unlink()

    def test_docstrings_present(self):
        pybytecompiler.do_compile_directory(str(self.source_file_path.parent))
        with self.source_file_compiled.open(mode="rb") as sfc:
            file_contents = sfc.read()

        self.assertNotIn(pybytecompiler.main.__doc__.encode(), file_contents)
