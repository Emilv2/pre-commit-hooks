from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import io
import sys
import configparser
from typing import Optional
from typing import Sequence


def main(argv=None):  # type: (Optional[Sequence[str]]) -> int
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='XML filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        try:
            with io.open(filename, 'rb') as ini_file:
                configparser.RawConfigParser().read_file(ini_file)
        except configparser.ParsingError as exc:
            print('{}: Failed to ini parse ({})'.format(filename, exc))
            retval = 1
    return retval


if __name__ == '__main__':
    sys.exit(main())
