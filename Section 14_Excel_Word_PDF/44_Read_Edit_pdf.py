import PyPDF2
import os
os.chdir('c:\\users\\Mason\documents')
pdfFile = open('meetingminutes1.pdf', 'rb') # read binary mode
reader = PyPDF2.PdfFileReader(pdfFile)
reader.numPages
# 19
page = reader.getPage(0)
page.extractText()
for pageNum in range(reader.numPages):
	print(reader.getPage(pageNum).extractText())

