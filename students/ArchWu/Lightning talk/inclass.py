import sys

def main():
    switch = {
        "1": one,
        "2": submenu,
        "3": quit
    }
    
    while True:
        try:
            choice = input("Select 1-3 > ")
            if choice not in switch.keys():
                print("choose again")
            else:
                switch[choice]
        except SystemExit as e:
            break
def submenu():

def goodbye