#!/usr/bin/env python3

import argparse
import gzip
import logging
import re
import sys
import vl_convert as vlc

def process_arguments():
    parser = argparse.ArgumentParser(description='Test program to reproduce vl-convert issue #67')
    parser.add_argument('--rounds', type=int, default=6, help='How many rounds to run. Default: 6.')
    parser.add_argument('filenames', type=str, metavar='FILENAME', nargs='+')
    return parser.parse_args()

def main():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    args = process_arguments()

    logging.info("Will run %d rounds.", args.rounds)
    for i in range(args.rounds):
        logging.info("Running round %d...", i+1)
        process_files(args.filenames)
        logging.info("Done with round %d.", i+1)
    logging.info("ALL DONE")

def process_files(filenames):
    for filename in filenames:
        logging.info("Processing %s...", filename)
        process_file(filename)
        logging.info("Processed %s.", filename)

def process_file(filename):
    basename = re.sub(r'\.json.gz$', '', filename)
    with gzip.open(filename, 'rt') as i:
        spec = i.read()
        write_svg(spec, f'{basename}.svg')
        write_png(spec, f'{basename}.png')

def write_svg(spec, svgname):
    with open(svgname, 'wt') as o:
        logging.info('Writing to %s...', svgname)
        svg = vlc.vegalite_to_svg(spec)
        o.write(svg)

def write_png(spec, pngname):
    with open(pngname, 'wb') as o:
        logging.info('Writing to %s...', pngname)
        png = vlc.vegalite_to_png(spec)
        o.write(png)


if __name__ == "__main__":
    main()