#!/usr/bin/env python

#Written by Lane M. Atmore Mar 2021

#required python packages
#pandas
#lxml

#Outputs a metadata file and individual text files for each article in the Factiva html output
#that are coded by index
#designed for converting Factiva html to TXM input
#http://textometrie.ens-lyon.fr/?lang=en

#to run: python \path\to\html_parser.py \path\to\html.html
#all files will be created in the same directory as where the script is run

import pandas as pd
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('HTML', help = 'Give the path to the html file you would like to parse')
args = parser.parse_args()

HTML = str(sys.argv[1])

factiva = pd.concat([art for art in pd.read_html(HTML, index_col=0)if 'HD' in art.index.values], axis=1).T.set_index('AN')
factiva = factiva.reset_index()
factiva.index = np.arange(1, len(factiva) + 1)
factiva['ID'] = factiva.index

meta_data = factiva[['ID', 'HD','BY','WC','PD','SN']]
meta_data.to_csv('Metadata.csv', sep = ',', index = False, header = True)

articles = factiva[['LP','TD']]

for row in articles.itertuples():
	with open(str(row.Index) + '.txt', 'w', encoding = 'UTF-8') as f:
		LP = str(row.LP)
		TD = str(row.TD)
		f.write('LP: ' + LP + '\n')
		f.write('TD: ' + TD)
