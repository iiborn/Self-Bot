import os
os.system("clear")
print("This is such a small script to run your self bot.")
print()
status = input("what kind of os are you using?(ubuntu/arch/fedora) ")
while True:
    if status == "ubuntu":
        os.system("screen ./launch.sh")
    elif status == "arch":
        os.system("screen ./launch_arch.sh")
    elif status == "fedora":
        os.system("screen ./launch_fedora.sh")
    else:
        status = input("You want to leave?(y/n) ")
        if status == "y": break
    status = input("#BEAT BOT TEAM :)#")
    
