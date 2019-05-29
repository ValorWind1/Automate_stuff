import re
"""
| = known as a pipe , = represents or 
"""
h = re.compile(r"Batman|Superman")
txt = h.search("some of my favorite super heroes are Batman and Superman")
print(txt.group())

print("----------------------")
# because its or , as soon as it finds the first element it will return it. for ex: another one
txt1=h.search("some of my favorite super heroes are Superman and Batman")
print(txt1.group())
print("------------------------")

"""
using pipe to find several patterns parts for ex : 
Batman', 'Batmobile', 'Batcopter', and 'Batbat'. Since all these strings start with Bat
"""

bats = re.compile(r'Bat(man|mobile|copter|bat)')
txt3 = bats.search("Batmobile lost a wheel")
print(txt3.group())
print(txt3.group(1))
