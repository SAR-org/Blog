
from pdf2image import convert_from_path
#from PIL import Image



def savePdfPageAsImage(pdfFilePath,imageFilePath):
    screenShotPageNum = input("Enter the page number that you want to take screenshot : ")
    print("Taking screenshot please wait.........")
    images = convert_from_path(pdfFilePath)
    screenshotFilePath = imageFilePath+"screenshot_"+screenShotPageNum+".jpg"
    images[int(screenShotPageNum)-1].save(screenshotFilePath, 'JPEG')

if __name__ == "__main__":
    dir = '/home/rajeevan/Documents/Rajeevan/StoyBooks/Downloads/'
    savePdfPageAsImage(dir+'test.pdf',dir)