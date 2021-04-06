# factiva_html_parser

This script is designed to parse Factiva html files for input into TXM: http://textometrie.ens-lyon.fr/?lang=en \
It will give you a metadata file with the following headers: ID, HD, BY, WC, PD, SN \
and individual text files for each of the articles with the name of the files coded by ID (Article 1 in the metadata matches article 1.txt) 


html_parser_windows.py has RN coded line endings (for Windows)\
html_parser_unix.py has LF coded line endings (for Mac/Linux)\
Make sure you download the version for your OS

Required python packages: \
pandas \
lxml

It is very simple to run the html parser. Simply move to the directory where you would like your output files and call the program as follows: \
python /path/to/html_parser_unix.py /path/to/html_file.html
