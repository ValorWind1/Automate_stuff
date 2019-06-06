import pyperclip
import re

#getting all the phone numbers
phone_re = re.compile(r'''((\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))?)''',re.VERBOSE)

# (\d{3}|\(\d{3}\))? = first 3 numbers. nongreedy
#((\s|-|\.) = separator dash " - "



#getting all the email adress
email_re = re.compile('''([a-zA-Z0-9._%+-]+@[a-zA-ZA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''',re.VERBOSE)

msg = str(pyperclip.paste())
matches = []
for i in phone_re.findall(msg):
    phone_num = "-".join([i[1],i[3],i[5]])
    if i[8]!= "":
        phone_num += "x" + i[8]
    matches.append(phone_num)
for i in email_re.findall(msg):
    matches.append(i[0])

if len(matches) >0:
    pyperclip.copy("\n".join(matches))
    print("Successful Copy to CP")
    print("\n".join((matches)))
else:
    print("No Phone numbers or email adresses found.")