import argparse
import io
import sys
from google.cloud import vision

def detect_text(path, out):
    if out == 0:
        out = "./textOutput/"+path+"_out.txt"

    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    sys.stdout = open(out, "w")
    for text in texts:
        print('\n"{}"'.format(text.description))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    sys.stdout.close()
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="The image for text detection.")
    parser.add_argument("-out_file", help="Optional output file", default=0)
    args = parser.parse_args()
    detect_text(args.filepath, args.out_file)





