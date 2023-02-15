import time
from datetime import datetime

def boot():
    print("Booting From Hardisk")
    time.sleep(3)
    now = datetime.now()
    hour = now.hour
    greeting = get_greeting(hour)
    print(greeting)
    menu()
    
def get_greeting(hour):
    if hour >= 5 and hour < 12:
        return "Good morning!"
        time.sleep(2)
        menu()
    elif hour >= 12 and hour < 18:
        return "Good afternoon!"
        time.sleep(2)
        menu()
    elif hour >= 18 and hour < 22:
        return "Good evening!"
        time.sleep(2)
        menu()
    else:
        return "Good night!"
        time.sleep(2)
        menu()
    
    
def menu():
    print("""
░█████╗░░█████╗░███╗░░░███╗░█████╗░░██████╗
██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██╔████╔██║██║░░██║╚█████╗░
██║░░██╗██║░░██║██║╚██╔╝██║██║░░██║░╚═══██╗
╚█████╔╝╚█████╔╝██║░╚═╝░██║╚█████╔╝██████╔╝
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝░╚════╝░╚═════╝░""")
    menu = input("COMOS/KERNEL/OS.OSF>>>")
    if menu == "disk'comos','start','fmanager'":
        fmanager()
        
    if menu == "disk'comos','start','games'":
        games()
        
    if menu == "disk'comos','start','browser'":
        browser()
        
    if menu == "disk'comos','start','office'":
        office()
    
    else:
        goback()
        
        
def goback():
    menu()
    
def office():
    print("""
░█████╗░███████╗███████╗██╗░█████╗░███████╗
██╔══██╗██╔════╝██╔════╝██║██╔══██╗██╔════╝
██║░░██║█████╗░░█████╗░░██║██║░░╚═╝█████╗░░
██║░░██║██╔══╝░░██╔══╝░░██║██║░░██╗██╔══╝░░
╚█████╔╝██║░░░░░██║░░░░░██║╚█████╔╝███████╗
░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝░╚════╝░╚══════╝""")
    print("COMOS/KERNEL/GAMES")
    print(" ")
    print("[1]COMOS-Presentation")
    print("[2]Web-Maker")
    print("exit [sends you to the menu]")
    office = input("COMOS/KERNEl/OFFICE>>>")
        
    if office == exit:
        menu()
        
    else:
        gobackoffice()
        
def gobackoffice():
    office()
    
    
def browser():
    print(" ")
    goback()
        
def games():
    print("""
░██████╗░░█████╗░███╗░░░███╗███████╗░██████╗
██╔════╝░██╔══██╗████╗░████║██╔════╝██╔════╝
██║░░██╗░███████║██╔████╔██║█████╗░░╚█████╗░
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░░╚═══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██████╔╝
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░""")
    print("COMOS/KERNEL/GAMES")
    print(" ")
    print("[1]Revolutionary")
    print("[2]Dark Rooms")
    print("exit [sends you to the menu]")
    gamessel = input("COMOS/KERNEl/FILE/SELECT.sff>>>")
    if gamessel == "1":
        revolutionary()
    
    if gamessel == "2":
        menu()
    
            
    if gamessel == "exit":
        menu()
    
def revolutionary():
    print("Revolutionary")
    print("By Interlite Entertainment")
    print(" ")
    print("Please put in your code to verify your copy of Revolutionary!")
    code = input("code>>>")
    if code == "exit":
        menu()
    else:
        revolutionary()
        
def fmanager():
        print("""
███████╗███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗██████╗░
██╔════╝████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝██╔══██╗
█████╗░░██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██████╔╝
██╔══╝░░██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██╔══██╗
██║░░░░░██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝""")
        print("COMOS/KERNEL/FILES")
        print(" ")
        print("[1]readme.txt")
        print("exit [sends you to the menu]")
        fman = input("COMOS/KERNEl/FILE/SELECT.sff>>>")
        if fman == "1":
            readme()
            
        if fman == "exit":
            menu()

def readme():
    print("thank you for using Command OS also know as COMOS! Your Version Is Alpha!")
    print("We could not find your computer type though so please enter your computer type in edit so we can use this infomation for more functionality")
    print("From COMOS team in Interlite Inc.")
    rm = input("?>>>")
    if rm == "edit":
        error()
        
    if rm == "exit":
        menu()
    
    else:
        
        readme()
    
    
def error():
    print("Error With Disk Or Software")
    errorinput = input("COMOS/KERNEL/OS.OSF>>>")
    if errorinput == "reset":
        boot()
    else:
        error()
        
boot()




