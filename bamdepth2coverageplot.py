#!/usr/bin/env python

import argparse, pandas as pd, matplotlib.pyplot as plt

# command line parsing info
parser = argparse.ArgumentParser(description='Create coverage plot')
parser.add_argument('-b', '--bamdepth', type=argparse.FileType('r'), required=True, help='samtools depth output file')
parser.add_argument('-s', '--sample', type=str, required=True, help='sample name')
parser.add_argument('-f', '--filetype', type=str, default='png', help='output filetype (default: png)')
args = parser.parse_args()

def covergage_plot():
  with args.bamdepth as file:
    depth = pd.read_csv(args.bamdepth, header=None, names=['Contig', 'Position', 'Depth'], sep="\t")

  sample = args.sample
  filetype = args.filetype
  outname = '.'.join([sample, filetype])

  # TODO loop through possible contigs
  plt.bar(x='Position', height='Depth', width=1, data=depth, color='black')
  plt.xlabel('Genomic Position')
  plt.ylabel('Read Depth')
  plt.title(sample)
  plt.savefig(outname, format=filetype)

covergage_plot()
