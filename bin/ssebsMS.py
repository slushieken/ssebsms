###
#   ssebsMS.py - ssebsMS cli utility
#   (c) 2018 - Sebastian Safari - FOSS MIT License
###

## handle imports ##
import os,sys
sys.dont_write_bytecode=True    # disable .pyc files

from markdown import markdown
from _init import init_test, init_entry
from _build import build_test, build_entry
from _clean import clean_test, clean_entry
from _run import run_entry

## help output below (future commands to support) ##
env_filename = "ENV-ssebsMS"
help_output = '''ssebsMS.sh <CMD> [site-name]

Possible CMD's:
    init        <- initialize a new ssebsMS website
    build       <- build current website
    clean       <- clean generated files (delete for now)
    remove      <- remove ssebsMS website
    run <port>  <- run a local instance of your website
    help        <- output this help page

ENV file:
    ''' + env_filename + '''    <- Modify this file so you don't have to specify [site-name] in every command.
'''
## main function ##
def main(argv):
    # choose what to do next depending on arg
    cmd = get_args(argv)

    # TODO: Add checks for build / run to make sure site is actually there

    if "init" in cmd:
        print("Initializing " + cmd[1] + "website...")
        init(cmd[1])
        print(cmd[1] + " website initialized.")
    elif "build" in cmd:
        print("Building " + cmd[1] + " website...")
        build(cmd[1])
        print(cmd[1] + " website built.")
    elif "clean" in cmd or "remove" in cmd:
        print("Cleaning " + cmd[1] + " website...")
        clean(cmd[1])
        # TODO: have a clean and a delete
        print(cmd[1] + " website cleaned.")
    elif "run" in cmd:
        print("Running website at " + cmd[1] + "/public")
        try:
            run(cmd[1], int(cmd[2]))
        except IndexError:
            run(cmd[1])
    else:
        print(help_output)
        exit(1)

# end main

## initialization of website data ##
def init(site_name):
    #init_test("ssebs_init")
    init_entry(site_name, env_filename)
    pass
# end init()

## build existing website content
def build(site_name):
    #build_test("ssebs_build")
    build_entry(site_name)
    pass
# end build()

## run - server site
def run(site_name,port=8008):
    run_entry(site_name,port)
# end run()

# clean generated website
def clean(site_name):
    #clean_test("ssebs_clean")
    clean_entry(site_name, env_filename)
    pass
# end clean

# check local environment file
def get_env_var():
    ret = ""
    has_var = False
    if env_filename in os.listdir("./"):
        with open(env_filename, "r") as f:
            # print("Contents of " + env_filename + ":")
            for l in f:
                if not l.startswith("#"):
                    # print("config line: " + l.strip("\n"))
                    if l.startswith("site-name"):
                        tmp = l.split("=")[1].strip()
                        ret = tmp
                        has_var = True
    if not has_var:
        ans = input("Are you sure you want to use the default site at 'my_site/'? ")
        if 'y' in ans.lower():
            ret = "my_site"
        else:
            print("Please add a site name to the end of your command. e.g. 'ssebsMS.py CMD site-name'\n")
            exit(1)
    return ret
# end get_env_var()

## get args from cli ##
def get_args(argv):
    num_arg = len(sys.argv)
    cmd_arg = [None, None]

    if num_arg == 1:    # ssebsMS.py 
        return ""
    elif num_arg == 2:  # ssebsMS.py CMD
        cmd_arg = [sys.argv[1], get_env_var()]
    elif num_arg == 3:  # ssebsMS.py CMD site-name
        if sys.argv[2].isdigit():
            print("ISDIGIT: " + str(sys.argv))
            cmd_arg = [sys.argv[1], get_env_var(), sys.argv[2]]
        else:
            cmd_arg = [sys.argv[1], sys.argv[2]]
    elif num_arg == 4:  # ssebsMS.py run? site-name port?
        cmd_arg = [sys.argv[1], sys.argv[2], sys.argv[3]]
    else:               # ssebsMS.py CMD site-name ??? ?? ?
        return ""
    return cmd_arg
# end get_args()

## main func def ##
if __name__ == "__main__":
    main(sys.argv)
