def isPhoneN(txt):
    if len(txt) != 12:
        return False

    for i in range(0,3):
        if not txt[i].isdecimal():
            return False

    if txt[3]!="-":
        return False

    for i in range(4 , 7):
        if not txt[i].isdecimal():
            return False

    if txt[7] != '-':
        return False

    for i in range(8,12):
        if not txt[i].isdecimal():
            return False

    return True

# print(isPhoneN("777-333"))
# # print(isPhoneN("111-333-5555"))

"""
finding in pattern in a paragraph

On each iteration of the for loop, a new chunk of 12 characters from message is assigned to the variable chunk ❶. For example, 
on the first iteration, i is 0, and chunk is assigned message[0:12] (that is, the string 'Call me at 4'). On the next iteration, i is 1,
and chunk is assigned message[1:13] (the string 'all me at 41').

You pass chunk to isPhoneNumber() to see whether it matches the phone number pattern ❷, and if so, you print the chunk.
"""

msg = "Text me at 555-666-7777 tonight. 555-666-1111 is my cell phone."
for i in range (len(msg)):
    chunk = msg[i:i+12]  #
    if isPhoneN(chunk):
        print("phone found :" + chunk)
print("completed")