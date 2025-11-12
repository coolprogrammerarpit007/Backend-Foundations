import re

# Search the string to see if it starts with "The" and ends with "Spain":

txt = 'The rain in Spain'
# txt = 'The rain in Egypt'
x = re.search("^The.*Spain$",txt)
# print(x)

# The re module offers a set of functions that allows us to search a string for a match:

# findall -> returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

# Character	Description	Example	
# []	A set of characters	"[a-m]"	
# \	Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	Any character (except newline character)	"he..o"	
# ^	Starts with	"^hello"	
# $	Ends with	"planet$"	
# *	Zero or more occurrences	"he.*o"	
# +	One or more occurrences	"he.+o"	
# ?	Zero or one occurrences	"he.?o"	
# {}	Exactly the specified number of occurrences	"he.{2}o"	
# |	Either or	"falls|stays"	
# ()	Capture and group	 	 


