#!/usr/bin/env python

import argparse, sys

# command line parsing info
parser = argparse.ArgumentParser(description='Calculate percent GC content for fasta sequences')
parser.add_argument('-s', '--sequences', type=argparse.FileType('r'), required=True, help='file of sequences, one per line (fasta files not currently supported')
args = parser.parse_args()

def get_gc_content():
    with args.sequences as file:
        for seq in file:
            nucleotides = {}
            seq = seq.strip()
            length = len(seq)
            for i in seq:
                nucleotides[i] = nucleotides.get(i, 0) + 1
            percent_GC = ((nucleotides.get('G', 0) + nucleotides.get('C', 0)) / length) * 100
            print(percent_GC)

get_gc_content()