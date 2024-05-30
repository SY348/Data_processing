import sys
import os
import pandas as pd
import numpy as np

if len(sys.argv) != 3:
	print("Usage: python merge_list.py <total_list> <file_name_list>")
	sys.exit(1)

whole_list = sys.argv[1]
whole_list = pd.read_csv(whole_list)

filenames = sys.argv[2]
filenames = pd.read_csv(filenames, header=None)[0].tolist()


for i in filenames:
	temp = pd.read_csv(i, sep='\t')
	whole_list= pd.merge(whole_list, temp, on='gene_name', how='outer')

whole_list.fillna(0,inplace=True)

print(whole_list)
