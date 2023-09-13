import re

text = "The price is $20.50"
match = re.search(r'\$\d+\.\d{2}', text)
print("Price:", match.group())
