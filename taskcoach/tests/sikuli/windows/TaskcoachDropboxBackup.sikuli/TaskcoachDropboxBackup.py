#from sikuli import *
#import TaskcoachMain
#def dropbox():
click("1385560224304.png")
type("cmd")
sleep(2)
type(Key.ENTER)
sleep(1)
type("cd .." + Key.ENTER)
type("cd .." + Key.ENTER)
type("cd Task-Coach-Evolution" + Key.ENTER)
type("cd taskcoach" + Key.ENTER)
type("python taskcoach.py" + Key.ENTER)
sleep(8)
assert exists ("1385718239031.png")
sleep(2)
type('d', KEY_ALT)
sleep(5)
if exists("1385765333899.png"):
    paste("1385766759856.png", "gula_bananen@msn.com")
    sleep(1)
    type(Key.TAB)
    type("ocicatleo" + Key.ENTER)
    sleep(3)
assert exists("1385765432378.png")
click("1385765458210.png")
sleep(2)
assert exists("1385765498459.png")
click("1385765531131.png")
sleep(2)
Region(457,333,456,130).click("1385772775833.png")
sleep(1)
assert exists("1385765661633.png")
click("1385765688747.png")
print("Successfully uploaded the tasks to Dropbox")
#closeApp()

#def closeApp():
sleep(1)
click("1385770367703.png")