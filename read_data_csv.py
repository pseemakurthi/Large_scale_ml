import os, csv
import pandas as pd
local_path = os.getcwd() 
source = 'hour.csv' 
SEP = ','

def read_using_csv_reader(local_path,source):
#if using python 2 add , 'rb' to the open argument in the below line4
	with open(local_path + '//' + source) as R:
		'''
		 read the file from using handle R
		'''

		file = csv.reader(R)

		for n, row in enumerate(file):
			#make first line as header
			if n == 0:
				header = row
			else :
				#do the pre-processing
				pass

		print('No. of lines in the file 	:{}'.format(n+1))
		print('Header 						:{}'.format(','.join(header)))
		print('Sample Record				:{}'.format(','.join(row)))


def read_using_pandas_io(local_path,source,CHUNK_SIZE = 1000):
	with open(local_path + '//' + source, 'rb') as R:
		iterator = pd.read_csv(R, chunksize = CHUNK_SIZE)

		for n, data_chunk in enumerate(iterator):
			print('{}th chunk '.format(n))
			print('Size of the uplodaed chunk {0} rows, {1} features'.format(data_chunk.shape[0], data_chunk.shape[1]))
			pass

		print("Sample values 		:{}".format(data_chunk.iloc[0]))





if __name__ == '__main__':
	read_using_pandas_io(local_path,source)
