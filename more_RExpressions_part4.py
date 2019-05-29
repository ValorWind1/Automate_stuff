import re

"""
Wilcard Character 
 the . (or dot) it will match any character except for a new line 
"""

dot = re.compile(r".at")
txt = dot.findall("the cat in the hat sat on the flat mat")
print(txt) # we get back all words with at in their words

print("---------------------------")
"""
Matching everything with Dot-Star 
dot-start = (.*). will match anything inside the dot and star parenthesis , or < > 
"""

anything_dot_star = re.compile(r"First Name: (.*) Last Name: (.*)")
txt2 = anything_dot_star.search("First Name: Alfonso Last Name: Alcantara")
print(txt2.group(1))
print(txt2.group(2))

# To match any and all text in a nongreedy fashion, use the dot, star, and question mark (.*?).
# ex :
nongreedy =re.compile(r"<.*?>")
txt3 = nongreedy.search("<To serve a man> for dinner>")
print(txt3.group())


print("---------------------")
"""
Matching new lines with dot characters 
re.DOTALL = match all characters including newline characters 
"""

nonewline = re.compile(r".*")
txt4 = nonewline.search("Serve the public trust.\nProtect the Innocent\nuphold the law")
print(txt4.group())

print("               ")
newline = re.compile(r".*",re.DOTALL)
txt5 = newline.search("Serve the public trust.\nProtect the Innocent\nuphold the law")
print(txt5.group())