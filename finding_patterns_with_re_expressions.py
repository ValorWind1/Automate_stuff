import re
"""
 \d means “a digit character” 
 
 Here, we pass our desired pattern to re.compile() and store the resulting Regex object in phoneNumRegex.
  Then we call search() on phoneNumRegex and pass search() the string we want to search for a match. 
  The result of the search gets stored in the variable msg.
 
"""

phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
msg = phoneRegex.search("My number is 914-432-2332")
print("Phone number found:" + msg.group())