"""Analysis checks for the output of the pybytecompile script
"""

import unittest

from compileall import compile_file
from pathlib import Path

from pybytecompile.bin import pybytecompile


class TestCompileOutput(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.source_file_path = Path(pybytecompile.__file__)
        self.source_file_compiled = self.source_file_path.parent.joinpath(
            ".".join([self.source_file_path.stem, "pyc"])
        )

    def tearDown(self):
        super().tearDown()
        if self.source_file_compiled.exists():
            self.source_file_compiled.unlink()

    def test_docstrings_present(self):
        pybytecompile.do_compile_directory(str(self.source_file_path.parent))
        with self.source_file_compiled.open(mode="rb") as sfc:
            file_contents = sfc.read()

        self.assertNotIn(pybytecompile.main.__doc__.encode(), file_contents)
