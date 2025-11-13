import re

# regular expressions allow us to match for a specific pattern. 

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
900*555*1234
900/555/1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to end!'

# print('\tTab')
# print(r'\tTab') -> raw string

# pattern = re.compile(r'abc')
# matches = pattern.finditer(text_to_search)
# # print(matches)

# for match in matches:
#     print(match)


# regex to match the phone number

# pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
# only to match number start from 800 or 900
# pattern = re.compile(r'[89]00[-.]\d{3}[-.]\d{4}')
# pattern = re.compile(r'[^b]at')
# matching pattern starts with Mr/Mrs/Mr
# pattern = re.compile(r'M[rs]s?\.?\s.+')
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s.+')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# open the file , then extract phone numbers

# with open('data.txt','r') as f_hand:
#     contents = f_hand.read()
#     mobile_number_pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
#     mobile_number_matches = mobile_number_pattern.finditer(contents)
    
#     for match in mobile_number_matches:
#         print(match)

