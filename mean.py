#!/usr/bin/env python

import os
import sys
import pandas as pd
import scipy.stats as stats

if len(sys.argv) != 3:
	print("Usage: python mean.py <sorted.pA> <sorted.pG>")
	sys.exit(1)

pd.set_option('display.max_rows',None)

inputfile_A = sys.argv[1]
inputfile_A = pd.read_csv(inputfile_A, sep='\t', header=None)
inputfile_A.columns = ['gene_name', 'pA_number']

inputfile_G = sys.argv[2]
inputfile_G = pd.read_csv(inputfile_G, sep='\t', header=None)
inputfile_G.columns = ['gene_name', 'pG_number']

for line in inputfile_A:
	A_mean = inputfile_A.groupby('gene_name')['pA_number'].mean().reset_index()

for line in inputfile_G:
	G_mean = inputfile_G.groupby('gene_name')['pG_number'].mean().reset_index()

merge = pd.merge(A_mean, G_mean, on='gene_name')
merge['G%']=merge['pG_number']/(merge['pA_number']+merge['pG_number']+1)*100

print (merge)
