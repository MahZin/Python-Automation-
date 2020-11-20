# function to get all of the text inside a word document as a string

import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs: # para = paragraph
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('c:\\users\\Mason\\documents\\demo.docx'))
