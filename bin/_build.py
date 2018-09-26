###
#   ssebsMS.py - ssebsMS cli utility
#   (c) 2018 - Sebastian Safari - FOSS MIT License
###

##
#   This file should be ran by the ssebsMS.py file
##

## _build.py file structure
# 1) imports
# 2) variable defs
# 3)
#

## Procedure on how pages will be built ##
# [ ] Check / read config file
# [ ] list dirs
# [ ] check for md files & make sure they match config
# [ ] loop through page md files and get file based configs
#   [ ] make list of page objects & set their settings
#   [ ] read contents of Markdown
#   [ ] generate html per page in public/ dir
# [ ] test to make sure pages are there

# 1 - imports
import os

# 2 - variable defs

# 3 -

# entry of build module
def build_entry(site_name):
    if site_name in os.listdir("./"):
        print(os.listdir("./" + site_name ))
    else:
        #print("ls: " + str(os.listdir("./")))
        print("No " + site_name + "/ directory found. Have you run 'ssebsMS.py init'? See help...")
# end entry()

# test definition for import testing
def build_test(my_arg):
    print("I'm in the _build.py file! Even " + str(my_arg) + " is here!")