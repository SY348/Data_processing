#!/usr/bin/env python

import os
import sys
import pandas as pd
import scipy.stats as stats

pd.set_option('display.max_rows',None)

inputfile = sys.argv[1]
inputfile = pd.read_csv(inputfile, sep='\t', header=None)
inputfile.columns = ['gene_name', 'pA_length']


for line in inputfile:
	input_mean = inputfile.groupby('gene_name')['pA_length'].mean().reset_index()
	input_mean['pA_length'] = input_mean['pA_length'].round()
	print(input_mean)
