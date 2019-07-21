from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt


# converts pdf, returns its text content as a string
class PdfToText:

    def convert(fname, pages=None):
        if not pages:
            pagenums = set()
        else:
            pagenums = set(pages)

        output = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)

        infile = open(fname, 'rb')
        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        output.close
        return text

    #converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
    def convertMultiple(pdfDir, txtDir):
        if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in
        for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
            fileExtension = pdf.split(".")[-1]
            if fileExtension == "pdf":
                pdfFilename = pdfDir + pdf
                text = PdfToText.convert(pdfFilename) #get string of text content of pdf
                textFilename = txtDir + pdf.split(".")[0] + ".txt"
                print (textFilename)
                textFile = open(textFilename, "w", encoding="utf-8") #make text file
                textFile.write(text) #write text to text file
        return textFile

# pdfDir = "C:/Users/Liza/Desktop/MajorCVAnalysis/Code/MajorProject/cv/"
# txtDir = "C:/Users/Liza/Desktop/MajorCVAnalysis/Code/MajorProject/text/"
# PdfToText.convertMultiple(pdfDir, txtDir)