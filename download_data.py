import urllib.request as urllib2
import os, requests, io
from io import StringIO as StringIO
import numpy as np 
import tarfile, gzip, zipfile

'''
 Utility for download various types for data from UCI repo
'''

def unzip_from_uci_data(UCI_URL, dest = ' '):
	'''
	Takes URL and dest as input and saves the data to disk at the given destination
	'''
	'''
		Get the response from the request
		save as raw byes and parse each url in the dataset
	'''

	response = requests.get(UCI_URL)
	compressed_file = io.BytesIO(response.content)
	z = zipfile.ZipFile(compressed_file)
	print("Extracting in {}".format(os.getcwd()))

	for name in z.namelist():
		if '.csv' in name:
			print("\t Extracting {} to {} location".format(name,os.getcwd()))
			z.extract(name,path = os.getcwd() + '\\' + dest)



def gzip_from_uci(UCI_URL, dest = ' '):

	response = urllib2.urlopen(UCI_URL)
	compressed_file = io.BytesIO(response.read())
	decompressed_file = gzip.GzipFile(compressed_file)
	filename = UCI_URL.split('/')[-1][:-3]

	with(os.getcwd() + '\\' + filename, 'wb') as outfile:
		outfile.write(decompressed_file.read())
	print('File {} decompressed'.format(filename))  


def tar_from_uci(UCI_URL, dest = ' '):
	response = urllib2.urlopen(UCI_URL)
	compressed_file = StringIO.StringIO(response.read())
	tar = tarfile.open(mode = 'r:gz',fileobj = compressed_file)
	tar.extractall(path = dest)
	datasets = tar.getnames()
	for dataset in datasets:
		size = os.path.getsize(dest + '\\' +dataset)
		print("File {0} size in {1} bytes  :".format(dataset,size))
	tar.close()



def load_matrix(UCI_URL):
	return np.load_matrix(urllib2.urlopen(UCI_URL))