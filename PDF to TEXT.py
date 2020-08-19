import PyPDF2

pdfFileObj = open('Macro.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print('Page No:', pdfReader.numPages)

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

pdfFileObj.close()
