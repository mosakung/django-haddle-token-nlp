import os
from pdf2image import convert_from_path

# poppler
# pdf2image

ROOT = os.path.abspath(os.getcwd())


def convertPdftoJpg(pathName, pdfName, startPage):
    # define the name of the directory to be created
    path = ROOT + "/document-image/" + pdfName
    try:
        os.mkdir(path)
        print("Successfully created the directory %s" % path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Already have the directory %s" % path)
    poppler_path = ROOT+"\ocr\poppler-0.68.0\\bin"
    pages = convert_from_path(
        pathName, dpi=300, poppler_path=poppler_path, size=(2000, None))
    count = startPage
    for index, page in enumerate(pages):
        if index+1 >= startPage:
            page.save(path+'/page'+str(count)+'.jpg', fmt='jpg')
            count = count+1
