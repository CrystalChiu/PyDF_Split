from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('pdf_name')
parser.add_argument('new_folder')
args = parser.parse_args()

pdf_name = args.pdf_name
new_folder = args.new_folder

inputpdf = PdfFileReader(open(pdf_name, "rb"))

if(os.path.exists(new_folder) is False):
    print(f"Creating new folder at {new_folder}...")
    os.mkdir(new_folder)


for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open(f"{new_folder}/{i+1}_{pdf_name}", "wb") as outputStream:
        output.write(outputStream)