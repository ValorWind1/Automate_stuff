import re
"""
The regular expression \d+\s\w+ will match text that has one or more numeric digits (\d+), 
followed by a whitespace character (\s), followed by one or more letter/digit/underscore characters (\w+).
"""
m = re.compile(r"\d+\s\w+")
txt=m.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids,\
 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(txt)

print("------------------")
"""
making your own character classes 
find what you want 
"""

vowels = re.compile(r"[aeiouAEIOU]")
txt1=vowels.findall("ana loco lebron james cristiano messi")
print(txt1)


nums = re.compile(r"[123456789]")
txt2 = nums.findall("f1nding al1 th3 numb3er5 in5id3 7eacher")
print(txt2)

print("----------------------")
"""
making a negative character class with ^ . 
meaning A negative character class will match all the characters that are not in the character class
"""

negative=re.compile(r"[^aeiouAEIOU]")
txt3 = negative.findall("ana loco lebron james cristiano messi")
print(txt3)

print("---------------------")
"""
Caret and Dollar Sign Characters 
You can also use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of 
the searched text. Likewise,
 you can put a dollar sign ($) at the end of the regex to indicate the string must end with this regex pattern
"""
beginsWith = re.compile(r"Hello")
beginsWith.search("Hello World!")
print(beginsWith.search("He said hello") == None)

endsWith =re.compile(r"\d$")
endsWith.search("Your Number is 42")
print(endsWith.search("Your number is forty two")== None)


wholeString = re.compile(r"^\d+$") # matches strings both begin and end with
wholeString.search("1234567890")
print(wholeString.search("12345vs67890")==None)
print(wholeString.search("12 34567890")==None)

# this examples show how the strings must match extacly when we inplement ^ and $

