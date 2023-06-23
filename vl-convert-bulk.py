#!/usr/bin/env python3

import gzip
import logging
import re
import sys
import vl_convert as vlc

def main():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    for filename in sys.argv[1::]:
        logging.info("Processing %s...", filename)
        process_file(filename)
        logging.info("Processed %s.", filename)
    logging.info("ALL DONE")

def process_file(filename):
    basename = re.sub(r'\.json.gz$', '', filename)
    svgname = f'{basename}.svg'
    with gzip.open(filename, 'rt') as i:
        spec = i.read()
        with open (svgname, 'wt') as o:
            logging.info('Writing to %s...', svgname)
            svg = vlc.vegalite_to_svg(spec)
            o.write(svg)

if __name__ == "__main__":
    main()