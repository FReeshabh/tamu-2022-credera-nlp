from pdfminer.high_level import extract_text
import sys
import argparse


def extractTextFromPdf(filepath):
    try:
        extracted_text = extract_text(filepath)
        outputFile = "./textOutput/"+filepath+"_pdf.txt"
        sys.stdout = open(outputFile, "w")
        print(repr(extracted_text))
        sys.stdout.close()
    except:
        raise Exception('Could not READ PDF')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="The PDF for text detection.")
    args = parser.parse_args()
    extractTextFromPdf(args.filepath)


