#!/usr/bin/env python

import argparse

# command line parsing info
parser = argparse.ArgumentParser(description='Determine how many reads to simulate to obtain a specific coverage')
parser.add_argument('-s', '--sequence', type=argparse.FileType('r'), required=True, help='sequence (does not currently support fasta files)')
parser.add_argument('-c', '--coverage', type=int, required=True, help='desired read depth/coverage of simulated reads')
parser.add_argument('-r', '--read_length', type=int, required=True, help='desired read length of simulated reads')
parser.add_argument('-p', '--paired', action="store_true", help='specify if desired simulated reads are to be paired end')

args = parser.parse_args()

def calculate_coverage():
	with args.sequence as file:
		for sequence in file:
			sequence = sequence.strip()
			length = float(len(sequence))
			coverage = float(args.coverage)
			read_length = float(args.read_length)
			count = (coverage * length) / read_length
			
			if args.paired:
				print(int(round(count / 2)))
			else:
				print(int(round(count)))

calculate_coverage()