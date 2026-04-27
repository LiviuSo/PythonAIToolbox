## TMInitiatesScanner
Utility to extract data from the scanned paper forms filled by handwriting.

### TODOs
- Create a shell script
- Add visual UI

### Limitations
The data extractor accepts three types of input;
- images (but with all util info of an initiate in one image)
- PDF files (but with all util info opf an initiate in one PDF file)
- unique PDF(but with all util info of an initiate on one page in the PDF)

### Usage
- place the input in the `data` folder in any of `images`, `pdfs` or `pdf` subfolder depending of the type of the input (see [Limitations](#limitations)) 
- Run the `main.py` in the project root folder uncommenting the appropriate filepath`
### Possible issues
- openpyxl is not installed:
```
# from project root
source .venv/bin/activate
python -m pip install openpyxl
```