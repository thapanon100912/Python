# Calculator.py
# Version 10.5
VERSION = "10.5"

# Import things
import math
import time
import os
import json

# Configs
VERSION_MESSAGE = f"Version {VERSION} : What's new"
SLEEP_TIME = 1
CLOSE_TIME = 4
VALUEERROR = "Unknown Value: Please Type Again"
ZERODIVISIONERROR = "Have Something Error: Cann't divided by 0"

# DataFile
DataFile = {
    "Histories" : []
}

# Number Functions
def Ask2number() :
    # Ask
    while True :
        try :
            print("\n")

            #Ask A
            a = float(input("A = "))
            print(a,"\n")

            #Ask B
            b = float(input("B = "))
            print(b,"\n")

            break
        except ValueError :
            print(VALUEERROR)
    
    return a, b

def Ask1number() :
    # Ask
    while True :
        try :
            print("\n")

            #Ask A
            a = float(input("A = "))
            print(a,"\n")

            break
        except ValueError :
            print(VALUEERROR)
    
    return a

# Operator Functions
def Plus() :
    try :
        # Ask
        a, b = Ask2number()

        # Calculate
        Answer = a + b
        
        #Float -> Int
        if Answer == int(Answer) :
            Answer = int(Answer)

        # Show Answer
        time.sleep(SLEEP_TIME)
        print ("Answer =" , Answer ,"\n\n")

        # Save
        DataFile["Histories"].append(f"{a} + {b} = {Answer}")
    except Exception as Reason :
        print("Have Something Error :" , Reason)

def Minus() :
    try :
        # Ask
        a, b = Ask2number()
        
        # Calculate
        Answer = a - b

        #Float -> Int
        if Answer == int(Answer) :
            Answer = int(Answer)

        # Show Answer
        time.sleep(SLEEP_TIME)
        print ("Answer =" , Answer ,"\n\n")

        # Save
        DataFile["Histories"].append(f"{a} - {b} = {Answer}")
    
    except Exception as Reason :
        print("Have Something Error :" , Reason)

def Times() :
    try :
        # Ask
        a, b = Ask2number()
        
        # Calculate
        Answer = a * b
        
        #Float -> Int
        if Answer == int(Answer) :
            Answer = int(Answer)

        # Show Answer
        time.sleep(SLEEP_TIME)
        print ("Answer =" , Answer ,"\n\n")

        # Save
        DataFile["Histories"].append(f"{a} * {b} = {Answer}")

    except Exception as Reason :
        print("Have Something Error :" , Reason)

def Divide() :
    try :
        # Ask
        a, b = Ask2number()
        
        # Calculate
        Answer = int(a // b)
        Remander = int(a % b)
        Answer_WithDecemal = a / b
        
        #Float -> Int & # Show Answer
        time.sleep(SLEEP_TIME)

        if Remander == 0 :
            print ("Answer =" , Answer ,"\n\n")
        elif Remander != 0 :
            print ("Answer =" , Answer)
            print ("Remander =" , Remander ,"\n")

            if input() == "=" : ## Plus
                time.sleep(SLEEP_TIME)
                print ("\nAnswer =" , Answer_WithDecemal ,"\n\n")
        else : raise

        # Save
        DataFile["Histories"].append(f"{a} / {b} = {Answer_WithDecemal}")
    except ZeroDivisionError :
        print(ZERODIVISIONERROR)
    except Exception as Reason :
        print("Have Something Error:" , Reason)

def Power() :
    try :
        # Ask
        a, b = Ask2number()
        
        # Calculate
        Answer = math.pow(a,b)
        
        #Float -> Int
        if Answer == int(Answer) :
            Answer = int(Answer)

        # Show Answer
        time.sleep(SLEEP_TIME)
        print ("Answer =" , Answer ,"\n\n")

        # Save
        DataFile["Histories"].append(f"{a} ^ {b} = {Answer}")

    except Exception as Reason :
        print("Have Something Error :" , Reason)

def Root() :
    try :
        # Custom Ask
        while True :
            try :
                print("\n")

                #Ask A
                a = input("Sqr, Cqr = ")

                #Check A -> Sqr = True, Cqr = False
                if a == "Sqrt" or a == "2":
                    a = "Sqrt"
                elif a == "Cbrt" or a == "3" :
                    a = "Cbrt"
                else :
                    raise ValueError
                
                print(a,"\n")

                #Ask B
                b = float(input(a+" of "))
                print(b,"\n")

                break
            except ValueError :
                print(VALUEERROR)
        
        # Calculate
        if a == "Sqrt" :
            Answer = math.sqrt(b)
        if a == "Cbrt" :
            Answer = math.pow(b,1/3)
        
        #Float -> Int
        if Answer == int(Answer) :
            Answer = int(Answer)

        # Show Answer
        time.sleep(SLEEP_TIME)
        print ("Answer =" , Answer ,"\n\n")

        # Save
        DataFile["Histories"].append(f"{a} of {b} = {Answer}")

    except Exception as Reason :
        print("Have Something Error :" , Reason)

def Factorial() :
    try :
        # Ask
        a = Ask1number()
        
        # Calculate
        Answer = math.factorial(a)

        # Show Answer
        time.sleep(SLEEP_TIME)
        print ("Answer =" , Answer ,"\n\n")

        # Save
        DataFile["Histories"].append(f"{a}! = {Answer}")
    except Exception as Reason :
        print("Have Something Error :" , Reason)

# Save Functions
def SaveData(Data, file_address) :
    try :
        with open(file_address,"w") as file :
            json.dump(Data, file, indent= 4)
    except FileNotFoundError :
        print("Unable to save : Data dir has destroyed or don't have data dir \nFile is not save.")
    except Exception as Reason:
        print("Unable to save : " , Reason, "\nFile is not save.")

def GetData(file_address) :
    try :
        with open(file_address, "r") as file :
            data = json.load(file)
        return data
    except FileNotFoundError :
        print("Unable to save : Data dir has destroyed or don't have data dir \nFile is not save.")
    except Exception as Reason:
        print("Unable to getData : " , Reason, "\nFile is not save.")

def CreateDataFile(EmptyData) :
    try :
        global DataFile

        script_address = os.path.abspath(__file__) # Find Script Address
        script_dir_address = os.path.dirname(script_address) # Find Dir Of Scipt Address

        # Mk dir
        dir_address = os.path.join(script_dir_address, "Data") # Find Dir (Data Dir)

        #If dir isn't exist:
        if not os.path.exists(dir_address) :
            os.mkdir(dir_address)
        
        file_address = os.path.join(dir_address, "Data.json") # Find File (File to crate)
        
        #If file isn't exist:
        if not os.path.exists(file_address) :
            with open(file_address,"w") as file : #Create File
                file.write("")

            SaveData(EmptyData, file_address)
        else : DataFile = GetData(file_address) # If no: get data

        return file_address
    except Exception as Reason :
        print("Have Something Error :" , Reason)

# Functions
def WhatNew() :
    print("")
    print(
        "Version 10.0"
        "\n1. Change Code Stucture",
        "\n2. Change Some Feature", "\n"
    )
    print(
        "Version 10.5",
        "\n1. Add Save System",
        "\n2. Fixed Bug", "\n\n"
    )

def Move() :
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def ShowHistories() :
    global DataFile

    histories = DataFile["Histories"]

    # Show
    print("\n--- Calculation Histories ---")

    if len(histories) == 0 :
        print("~~ No history ~~")
    else :
        for i in range(len(histories)) :
            print(histories[i])

    print("------------------------------")

    # Del?
    if input("\n") == "-" :

        if input("\nAre you sure you want to clear histories? [y/n]\n= ").lower() == "y" :
            DataFile["Histories"] = []

            time.sleep(SLEEP_TIME)
            
            print("\nHistories cleared.\n\n")
        else :
            print("\n\n")

def Run(File_AddressToSave:str) :
    print(VERSION_MESSAGE)

    while True :
        Input = input("Plus, Minus, Times, Divide, Power, Root, !, Move, Histories, Leave\n= ").strip().lower() ## Guide | Input -> Remove Space -> lower

        ## Operations
        if Input in ("pl", "plus") :
            Plus()

        elif Input in ("mi", "minus") :
            Minus()

        elif Input in ("mu", "times") :
            Times()

        elif Input in ("di", "divide") :
            Divide()

        elif Input in ("ex", "power") :
            Power()

        elif Input in ("rt", "root") :
            Root()
        
        elif Input in ("!") :
            Factorial()
        
        ## Functions
        elif Input in ("move") :
            time.sleep(SLEEP_TIME)

            Move()

        elif Input in ("his", "histories") :
            time.sleep(SLEEP_TIME)

            ShowHistories()

        elif Input in ("leave", "exit") :
            SaveData(DataFile, File_AddressToSave)

            time.sleep(CLOSE_TIME)

            break
        elif Input in ("what's new", "whats new") :
            WhatNew()
        
        ## For Error
        else :
            print("\nError\n\n")

# Code
file_address = CreateDataFile(DataFile)
DataFile = GetData(file_address)

Run(file_address)