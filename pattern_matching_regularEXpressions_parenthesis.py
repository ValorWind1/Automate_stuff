import re

phone = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
msg = phone.search("My Telephone number is 914-894-3421")
print(msg.group(1))
print(msg.group(2))
print(msg.group())
print(" ----------------------- ")


msg.groups()
area,num = msg.groups()
print(area)
print(num)



print("-------------------")
"""
incase parenthesis come separetely (914)
"""
phone = re.compile(r"(\(\d\d\d\))-(\d\d\d-\d\d\d\d)")
msg = phone.search("My Telephone number is (914)-894-3421")   # (914)
print(msg.group(1))
print(msg.group(2))
print(msg.group())