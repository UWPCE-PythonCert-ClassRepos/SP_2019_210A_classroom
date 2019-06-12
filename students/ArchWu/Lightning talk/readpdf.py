#!/usr/bin/env python3
from PyPDF4 import PdfFileReader, PdfFileWriter, PdfFileMerger

"""
Install of pypdf4: pip3 install pypdf4
previous version PyPDF2
No dependencies
"""



def extract_information(pdf_path):
    """Get the information from a given pdf file"""
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
    
    txt = f"Information about {pdf_path}: Author: {information.author} Creator: {information.creator}"
    "Producer: {information.producer} Subject: {information.subject} Title: {information.title}"
    "Number of pages: {number_of_pages}"

    print(txt)
    return information

def rotate(pdf_path):
    """Rotate pages of input pdf file as user wish"""
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)
    # rotate the first page clockwise for 90 degrees 
    page_1 = pdf_reader.getPage(0).rotateClockwise(90)
    pdf_writer.addPage(page_1)
    # rotate the second page counter clockwise for 90 degrees 
    page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
    pdf_writer.addPage(page_2)
    # add third page without rotation
    pdf_writer.addPage(pdf_reader.getPage(2))

    with open('rotate_pages.pdf', 'wb') as fh:
        pdf_writer.write(fh)


def split(path, name_of_split):
    """Split a pdf into multiple pdfs which containing each of the pages"""
    read = PdfFileReader(path)
    # For each page in pdf, create a single file of that page
    for page in range(read.getNumPages()):
        # Create reader each time in loop to prevent a crash
        pdf = PdfFileReader(path)
        pdf_writer = PdfFileWriter()
        # Write page to file
        pdf_writer.addPage(pdf.getPage(page))
        # Setting output file name
        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

def merge(files):
    """Merge two or more pdfs into one"""
    # Setting the file name of output
    output = "PyPDF-Merging-Output.pdf"
    # Create the merger instance
    merger = PdfFileMerger(open(output, "wb"))
    # Opening two input files
    input1 = open(files[0], "rb")
    input2 = open(files[1], "rb")
    # Add the first 3 pages of input1 to output
    merger.append(fileobj=input1, pages=(0, 3))
    # Insert the first page of input2 into the output beginning after the second page
    merger.merge(position=2, fileobj=input2, pages=(0, 1))
    # Append entire input3 document to the end of the output document
    merger.append(input2)
    # Output and close the file
    merger.write(output)
    print("Output successfully written to", output)
    merger.close()

if __name__ == '__main__':
    path = 'Culling the Masses- Democratic Origins of Racist Immigration Policy Americas.pdf'
    path2 = 'samplepdf.pdf'
    path3 = 'hw1.pdf'
    files = [path2, path3]
    extract_information(path)
    extract_information(path2)
    extract_information(path3)
    rotate(path2)
    split(path2, 'splitted_pdf')
    merge(files)


"""
More features:
Watermark
Encryption
"""