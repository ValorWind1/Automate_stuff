import shutil , os, re


datePattern = re.compile(r"""^(.*?)((0|1)?\d)-((0|1)?\d-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$) """,re.VERBOSE)

# looping over the files in the working directory
for i in os.listdir("."):
    mo = datePattern.search(i)

#if files dont have date skip them
    if mo == None :
        continue
# Get the different parts of the filename
    before = mo.group(1)
    month = mo.group(2)
    day = mo.group(4)
    year = mo.group(6)

    after=mo.group(8)

# european style DD-MM-YYYY

    eurofile = before+day+"-"+month+"-"+year+after

# get full absolute file path
    absWorkingDir = os.path.abspath(".")
    american_file =os.path.join (absWorkingDir  ,"C:\\Users\\skyjd\\PycharmProjects\\Automate_stuff\\organizing files chap 9\\04-11-1994.txt" )
    eruope_file = os.path.join(absWorkingDir   ,  "C:\\Users\\skyjd\\PycharmProjects\\Automate_stuff\\organizing files chap 9\\test2.txt"  )


# renaming file
    print('renaming "%$" to "%s"...'%(american_file,eruope_file))
    shutil.move(american_file,eruope_file)