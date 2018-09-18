#!/usr/bin/env python
from __future__ import print_function
import argparse
import os
import random

SEED=212

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        description='Determine which IDs have not been used. Issue a requested number of IDs.\
        IDs are assumed to be 5 digit numbers 10000 - 99999.')
    arg_parser.add_argument('--used_ids',
                            default='ised_ids.txt',
                            type=str,
                            help='A file containing all used IDs. No headers, white space delimeted IDs.\
                            One or more per row.')
    arg_parser.add_argument('--number_of_ids',
                            default=1,
                            type=int,
                            help='A number of IDs to issue.')
    arg_parser.add_argument('--update_used_ids',
                            default=False,
                            action='store_true',
                            help='Flag to update the used ids file.')
    args = arg_parser.parse_args()
    random.seed(SEED)
    used_ids = []
    with open(args.used_ids) as f:
        for l in f:
            used_ids += l.rstrip('\n').split()
    all_ids = set(map(str, range(10000, 100000)))
    avail_ids = list(all_ids.difference(set(used_ids)))
    print('Number of avilable IDs: %s' % str(len(avail_ids)))
    random.shuffle(avail_ids)
    print('Requested IDs:')
    for i in range(args.number_of_ids):
        print(avail_ids[i])


    if args.update_used_ids:
        print('Updating used IDs file ...')
        with open(args.used_ids, 'a') as f:
            for i in range(args.number_of_ids):
                f.write(avail_ids[i] + '\n')
        print('Done.')

