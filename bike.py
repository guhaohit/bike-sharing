import math
import csv


def RMLSE():
	n=0
    reader = csv.reader(open('output.csv', 'rb'))
   	for line in reader:
       	n += 1