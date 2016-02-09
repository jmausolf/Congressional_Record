

# Welcome to the Congressional Record Collector

This package enables the download of the Congressional Record, currently between 2009 and 2016.

This package may not be suited to all purposes since it collects the entire record for a given day as a singular text file rather than individual speech files for specific parts of the congressional record or tags for given speakers.

Sunlight Foundation has a useful Congressional Record utility for this purpose.

If, however, you simply want to get the text of the Congressional Record, this package should suit your needs.


# Dependencies

To run this package, you will need several functions. 

1. This package was written on and assumes you are running a Mac system, not Linux.
2. This package requires an Anaconda Distribution of Python, either 2.7+ or 3.5+
	* see https://www.continuum.io/downloads

3. This package requires the python distribution of wget:
	
	- 	wget: 
	- 	Download the wget program zipfile:
			https://pypi.python.org/pypi/wget

	- 	Through your command line terminal, navigate to the folder 
		and in your terminal execute "python setup.py install"

4. This package requires pdftotext
	
	-	Consider using homebrew and the command 'brew install poppler' to get pdftotext.


# To Run

1. Git clone this repository:
	```git clone https://github.com/jmausolf/Congressional_Record```

2. Navigate to the Python Scripts folder in this repository and run either

	- ```python __Get_Congressional_Records_py3.py```

	**Or**

	- ```python __Get_Congressional_Records_py2.py```

	Depending on which version of Python you use. This will download the PDF's of the daily Congressional Record.


3. To convert these PDFs to text, run ```bash __Convert_pdf_to_txt.sh```


