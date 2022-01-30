# Invoicer
Invoicer is a CLI tool to parse invoices from *any* source in any *file format* into convenient digestable spreadsheetable csv formats.

Made by: **Rishabh Tewari**

## How invoicer works
The entire program is written in 100% pythonic python, which aside from sounding cool means we have a vast array of tools and cool technologies at my disposal.


1. Convert invoices into text!! To do this for images, I used Google Cloud Vision APIs to perform optical character and word recognition. For PDFs I used PDFMiner to extract the needed data
2. Use these text files to generate useful insights from the invoices to generate friendly and useful CSVs. For this I used Huggingface transformers, using a Pytorch setup. 
3. Profit??
