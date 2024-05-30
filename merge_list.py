#!/usr/bin/env python

import sys
import os
import openpyxl
import pandas as pd
import numpy as np

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

if len(sys.argv) != 3:
	print("Usage: python merge_list.py <total_list> <file_name_list>")
	sys.exit(1)

whole_list_file = sys.argv[1]
whole_list = pd.read_csv(whole_list_file)

filenames_file = sys.argv[2]
filenames = pd.read_csv(filenames_file, header=None)[0].tolist()

merge_df = whole_list.copy()

for filename in filenames:
	temp_df = pd.read_csv(filename, sep='\t')
	merge_df= pd.merge(merge_df, temp_df, on='gene_name', how='outer')

merge_df.fillna(0,inplace=True)

merge_df.to_csv('_merge.pA.txt', sep='\t',index= False)
