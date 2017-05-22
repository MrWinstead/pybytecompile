#!/usr/bin/env python3

import logging

from argparse import ArgumentParser
from enum import Enum
from sys import argv


class ArgumentName(Enum):
    """Container for all CLI argument names
    """
    verbose = "verbose"

_PROGRAM_ARGUMENTS = (
    (("-v", ArgumentName.verbose.value), {"action": "count"},),
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
    parser = get_argumentparser()
    args = parser.parse_args(raw_args)
    logging.debug("running with arguments %s", args)

if __name__ == "__main__":
    main(argv[1:])
