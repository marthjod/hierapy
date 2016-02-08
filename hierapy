#!/usr/bin/env python

import click
import sys
from parser.parser import HieraOutputParser


@click.command()
@click.option('--json/--python', help='Format output as JSON/Python', default=True)
@click.option('--debug', is_flag=True, default=False)
def convert(json, debug):
    """Convert Hiera output to JSON/Python"""

    inp = sys.stdin.read().strip()
    if debug:
        print "In:", inp
    parser = HieraOutputParser(text=inp, debug=debug)

    if debug:
        print "Out:",
    if not json:
        print parser.get_python()
    else:
        print parser.get_json()


if __name__ == "__main__":
    convert()

