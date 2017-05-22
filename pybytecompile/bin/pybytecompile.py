#!/usr/bin/env python3

import logging

from argparse import ArgumentParser
from compileall import compile_dir
from enum import Enum
from os import path
from sys import argv, exit

from pybytecompile.optimization_levels import OptimizationLevel

class ExitValues(Enum):
    """Application exit values
    """
    SUCCESS = 0


class ArgumentName(Enum):
    """Container for all CLI argument names
    """
    verbose = "verbose"
    directory = "directory"

_PROGRAM_ARGUMENTS = (
    (("-v", ArgumentName.verbose.value), {"action": "count", "default": 0,
                                          "required": False},),
    (("-d", ArgumentName.directory.value), {"required": True},),
)


def get_argumentparser() -> ArgumentParser:
    """Create a default argument parser
    :return: ArgumentParser
    """
    ap = ArgumentParser()
    for arg, kwarg in _PROGRAM_ARGUMENTS:
        ap.add_argument(*arg, **kwarg)

    return ap


def main(raw_args: list) -> int:
    """main function of the application
    :param raw_args: 
    :return: 
    """
    return_value = ExitValues.SUCCESS
    parser = get_argumentparser()
    args = vars(parser.parse_args(raw_args))
    logging.debug("running with arguments %s", args)

    full_path = path.abspath(args[ArgumentName.directory.name])

    logging.info("compiling directory '%s'", full_path)
    compile_dir(
        full_path,
        optimize=OptimizationLevel.FULL.value,
        force=True,
        ddir=".",
        legacy=True
    )

    return return_value.value

if __name__ == "__main__":
    exit(main(argv[1:]))
