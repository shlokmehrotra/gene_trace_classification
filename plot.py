

# ALL CURRENT CODE PROCESSES IS IN NOTEBOOK (ONLY USED IN READING DATA)

import numpy as np
import pandas as pd
import csv
arr = []
with open("data.csv", newline='' ) as csvfile:
	#first = csvfile.readlines()[0].split(',')
	#print(first)
	for row in csvfile.readlines()[1:5]:
		row = row.rstrip()
		arr.append(row.split(','))
		print(row)
	arr = np.array(arr)
	print(arr)
	dataframe = pd.DataFrame(arr, columns = "[gene_id,spot_id,time,spot_fluorescence]")
print(dataframe)
