import  re
"""
ignore Case matching 
"""

paragraph = re.compile(r"robocop",re.I)
txt= paragraph.search("Robocop is part man.part machine,all cop")
print(txt.group())

txt1=paragraph.search("ROBOCOP is part man,part machine, all cop")
print(txt1.group())

print ( "                      ")
"""
substituting Strings with the sub() method 

"""

subs = re.compile(r"agent \w+")
msg=subs.sub("Censored "," agent alice gave the secret documents to agent bob ")
print(msg)

# For example, say you want to censor the names of the secret agents by showing just the first letters of their names.
# To do this, you could use the regex Agent (\w)\w* and pass r'\1****'
sub_Names = re.compile(r"Agent (\w)\w")
msg1 = sub_Names.sub(r"\1****","Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent")
print(msg1)

print("            "
      "     ")

"""
Managing Complex Regular Expression 
using re.Verbose 
"""


