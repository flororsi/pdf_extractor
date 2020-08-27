from collections import namedtuple
import re

import pdfplumber
import pandas as pd

Line = namedtuple('Line', 'Total')

line_re = re.compile(r'\d \d{2,}')

def numbify(num):
    return float(num.replace('$', '').replace(',', ''))

with pdfplumber.open("invoice.pdf") as pdf:
    page = pdf.pages[0]
    text = page.extract_text(x_tolerance=2, y_tolerance=0)

data = []

with pdfplumber.open("invoice.pdf") as pdf:
    page = pdf.pages[0]
    text = page.extract_text(x_tolerance=2, y_tolerance=0)
    
    for line in text.split('\n'):
        if re.match(r'T\S{3}', line):            
            site = line
            line_info = Line(site)
            data.append(line_info)
            break

df = pd.DataFrame(data)
print(df)