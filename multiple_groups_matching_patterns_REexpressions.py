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


print("--------------------")
"""
Sometimes there is a pattern that you want to match only optionally. 
The ? character . will do the work for us 
ex : bat man / bat wo man 
"""

Bat_reg_expression= re.compile(r"Bat(wo)?man")
msg= Bat_reg_expression.search("comic adventures of Batman")
print(msg.group())
msg1 = Bat_reg_expression.search("Comic adventures of Batwoman")
print(msg1.group())

print("-----------------------")
"""
using ? 
Using the earlier phone number example, you can make the regex look for phone numbers that do or do not have an area code.
"""

phonere = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
phonemsg = phonere.search("My telephone number is 415-555-4242")
print(phonemsg.group())
phonemsg1 = phonere.search("my number is 555-4242")
print(phonemsg1.group())


print("-------------------------")
"""
The * (called the star or asterisk) means “match zero or more”—the group that precedes 
the star can occur any number of times in the text.

"""

bats = re.compile(r"Bat(wo)*man")
t = bats.search("the adventures of Batman")
print(t.group())

t1 = bats.search("the adventures of Batwoman")
print(t1.group())

t2 = bats.search("the adventures of Batwowowowowowowoman")
print(t2.group())

print("--------------------------")


"""
matching one or more with + .

he + (or plus) means “match one or more.” Unlike the star, which does not require its group to appear 
in the matched string, the group preceding a plus *****must appear at least once.***** 
"""

batr = re.compile(r"Bat(wo)+man")
tx = batr.search("The adventures of Batwoman")
print(tx.group())

tx1=batr.search("the adventures of Batwowowowowowowoman")
print(txt1.group())

tx2 = batr.search("the adventures of Batman")   # The regex Bat(wo)+man will not match the string 'The Adventures of Batman'
                                                # because at least one wo is required by the plus sign
print(tx2 == None)

