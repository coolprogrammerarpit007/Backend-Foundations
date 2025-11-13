import re

urls1 = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
# capturing domain and top-level domain name
pattern = re.compile(r'https?://(www\.)?(\w+)\.((com|gov))')

matches = pattern.finditer(urls1)
subbed_urls = pattern.sub(r'\2\3',urls1)
for match in matches:
    print(match.group(2))