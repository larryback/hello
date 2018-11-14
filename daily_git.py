import sys, os
import datetime

sa = sys.argv

now = datetime.datetime.now()
default_msg = "{} lecture".format(now.strftime("%Y-%m-%d"))

msg = default_msg
commit_msg = default_msg
has_msg = len(sa) >= 2

if has_msg:
    commit_msg = sa[1]

else:
    input_msg = input("Default Message?? (Yes: Enter or input message) ")
    if input_msg != "":
        commit_msg = input_msg

print("commit ....", commit_msg)
os.system("git add --all") 
os.system('git commit -am "{}"'.format(commit_msg)) 
os.system("git push")      

