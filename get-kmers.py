#!/usr/bin/env python

import argparse, sys

# command line parsing info
parser = argparse.ArgumentParser(description='Get kmers from sequence and optionally positions or counts')
parser.add_argument('-f', '--sequence', type=argparse.FileType('r'), required=True, help='sequence (does not currently support fasta files)')
parser.add_argument('-k', '--kmer_length', type=int, required=True, help='length of kmers to output')
parser.add_argument('-o', '--output', type=str, default='kmers', help='specify desired output: kmers = kmers only, positions = kmers with positions, counts = kmers with counts')
args = parser.parse_args()

def get_kmers(k=args.kmer_length, output=args.output):
    with args.sequence as file:
        k = int(k)
        count_dict = {}
        kmer_list = []
        for seq in file:
            seq = seq.strip()
            if output=='counts':
                # counts will be for all sequences in the sequence file (combined counts)
                for i in range(len(seq)-k+1):
                    kmer_list.append(seq[i:i+k])
                for kmer in kmer_list:
                    count_dict[kmer] = kmer_list.count(kmer)
            else:
                for i in range(len(seq)-k+1):
                    kmer = seq[i:i+k]
                    if output=='positions':
                        # positions will be separate for each line in the sequence file
                        print(",".join([kmer, str(i)]))
                    elif output=='kmers':
                        print(kmer)
                    else:
                        print("Error: output argument must be one of: kmers, positions, counts")
                        sys.exit()
        for kmer in count_dict:
            # counts will be for all sequences in the sequence file (combined counts)
            print(",".join([kmer, str(count_dict[kmer])]))

get_kmers()
