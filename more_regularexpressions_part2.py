import re

laugh = re.compile(r"(Ha){3}")
msg = laugh.search("HaHaHa")
print(msg.group())

msg1 = laugh.search("Ha")
print(msg1 == None)  #here, (Ha){3} matches 'HaHaHa' but not 'Ha'. Since it doesn’t match 'Ha', search()

#Since (Ha){3,5} can match three, four, or five instances of Ha in the string 'HaHaHaHaHa',
# you may wonder why the Match object’s call to group() in the previous curly bracket example returns
# 'HaHaHaHaHa' instead of the shorter possibilities.
# After all, 'HaHaHa' and 'HaHaHaHa' are also valid matches of the regular expression (Ha){3,5}.

print("---------------")
"""
Greedy and None Greedy Method 
"""
# by default regular expressions are greedy by default
#
greedy = re.compile(r"(HA){3,5}")
gr =greedy.search("HAHAHAHAHA")
print(gr.group())

# find the less amount
nongreedy = re.compile(r"(HA){3,5}?")
nongr = nongreedy.search('HAHAHAHAHA')
print(nongr.group())

print("---------------")
"""
Findall() Method.

While search() will return a Match object of the first matched text in the searched string,
 the findall() method will return the strings of every match in the searched string. 
"""

phoneregex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
txt1 = phoneregex.search("Your Cellphone number is : 312-456-7893, and my work telephone is : 212-345-6789")
print(txt1.group())  # see it just returns the first that finds

txt2= phoneregex.findall('"Your Cellphone number is : 312-456-7893, and my work telephone is : 212-345-6789')
print(txt2) # it returns everything as tuples , since it doesnt have groups

txt3 = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)") # has groups parenthesis, different than phoneregex
txt4 = txt3.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(txt4)




