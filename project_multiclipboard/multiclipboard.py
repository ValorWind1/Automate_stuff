import shelve,pyperclip,sys

multiclipboard = shelve.open("mcb")

if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
        multiclipboard[sys.argv[2]] = pyperclip.paste()   # current content in the clipboard
elif len(sys.argv) == 2:

    #list keywords and load content
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(multiclipboard.keys())))
    elif sys.arv[1] in multiclipboard:
        pyperclip.copy(multiclipboard[sys.argv[1]])


multiclipboard.close()
