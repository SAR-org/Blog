import webbrowser
import os

from PyPDF2 import PdfFileWriter, PdfFileReader

def openAFile(filePath):
    webbrowser.open_new(filePath)



def modifyPdf(filePath):
    for file in os.listdir(filePath):
        if file.endswith(".pdf"):

            sourceFile = filePath+file
            
            openAFile(sourceFile)

            pagenumbers = input("Enter page numbers to be deleted, comma seperated : ")
            pages_to_delete = [int(e) if e.isdigit() else e for e in pagenumbers.split(',')]
            
            
            newFilePath = filePath+"_"+file
            infile = PdfFileReader(sourceFile, 'rb')
            output = PdfFileWriter()
            for i in range(infile.getNumPages()):
                if i+1 not in pages_to_delete:
                    p = infile.getPage(i)
                    output.addPage(p)
            with open(newFilePath, 'wb') as f:
                output.write(f)

if __name__ == "__main__":
    modifyPdf('/home/rajeevan/Documents/Rajeevan/StoyBooks/Downloads/')
    #openAFile('/home/rajeevan/Documents/Rajeevan/StoyBooks/Downloads/test.pdf')