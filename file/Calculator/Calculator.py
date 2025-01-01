# Calculator.py
# Version 11.0
VERSION = "11.2"

# Import things
import math
import time
import os
import json

# Configs
VERSION_MESSAGE = f"Version {VERSION} : What's new"
SLEEP_TIME = 1
CLOSE_TIME = 4
VALUEERROR = "Invalid input!: Try again."
ZERODIVISIONERROR = "Cann't divided by 0!\n\n"
ERROR = "An expected error occurred:"

# DataFile
Data = {
    "SaveHistories" : True ,
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
        if Data["SaveHistories"] == True :
            Data["Histories"].append(f"{a} + {b} = {Answer}")
    except Exception as Reason :
        print(ERROR , Reason)

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
        if Data["SaveHistories"] == True :
            Data["Histories"].append(f"{a} - {b} = {Answer}")
    
    except Exception as Reason :
        print(ERROR , Reason)

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
        if Data["SaveHistories"] == True :
            Data["Histories"].append(f"{a} * {b} = {Answer}")

    except Exception as Reason :
        print(ERROR , Reason)

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
            print ("Answer =" , Answer_WithDecemal ,"\n\n")
        elif Remander != 0 :
            print ("Answer =" , Answer_WithDecemal, "\n")

            if input() == "=" : ## Plus
                time.sleep(SLEEP_TIME)

                print ("\nAnswer =" , Answer)
                print ("Remander =" , Remander ,"\n\n")
                
            

            
        else : raise

        # Save
        if Data["SaveHistories"] == True :
            Data["Histories"].append(f"{a} / {b} = {Answer}")
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
        if Data["SaveHistories"] == True :
            Data["Histories"].append(f"{a} ^ {b} = {Answer}")

    except Exception as Reason :
        print(ERROR , Reason)

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
        if b <= 0 :
            raise ValueError

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
        if Data["SaveHistories"] == True :
            Data["Histories"].append(f"{a} of {b} = {Answer}")

    except ValueError :
        print(f"{VALUEERROR}\n\n")
    except Exception as Reason :
        print(ERROR , Reason)

def Factorial() :
    try :
        # Ask
        a = Ask1number()
        
        if int(a) != a or math.fabs(a) != a:
            raise ValueError

        # Calculate
        Answer = math.factorial(int(a))

        # Show Answer
        time.sleep(SLEEP_TIME)
        print ("Answer =" , Answer ,"\n\n")

        # Save
        if Data["SaveHistories"] == True :
            Data["Histories"].append(f"{a}! = {Answer}")
    except ValueError :
        print(f"{VALUEERROR}\n\n")
    except Exception as Reason :
        print(ERROR , Reason)

# Save Class
class DataHandler :
    Address_script = os.path.abspath(__file__)
    Address_scriptFolder = os.path.dirname(Address_script)
    Address_dataCenter = os.path.join(Address_scriptFolder, "Data")
    
      
    def __init__(self, file_name:str) :
        # Save File Name
        self.__file_name = file_name
        self.__Address_file = os.path.join(self.Address_dataCenter, self.__file_name)

        # Check Folder
        if not os.path.exists(self.Address_dataCenter) :
            os.mkdir(self.Address_dataCenter)
        
        # Check File
        if os.path.exists(self.__Address_file) :
            self.EverExists = True
        else :
            self.EverExists = False
            
    def save(self, data) :
        try :
            with open(self.__Address_file, "w") as file :
                json.dump(data, file, indent=4) # Push
        except FileNotFoundError as e:
            print(f"Error saving data: File Not Found -- {e}")
        except Exception as e :
            print("Error saving data:", e)
    
    def get(self) :
        try :
            with open(self.__Address_file,"r") as file :
                data = json.load(file) # Pull
            return data # Send
        except FileNotFoundError as e:
            print(f"Error saving data: File Not Found -- {e} -- Restart the program.")
        except Exception as e :
            print("Error geting data:", e)

    def DoFirst(self, EmptyData) :
        if self.EverExists == False :
            self.save(EmptyData)
            return EmptyData
        else :
            return self.get()


# Functions
def WhatNew() :
    print("")
    print(
        "Version 11.0"
        "\n1. Add History System",
        "\n2. Fixed Bug", "\n"
    )
    print(
        "Version 11.2",
        "\n1. Add Toggle History System", "\n\n"
    )

def Move() :
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def ShowHistories() :
    global Data

    histories = Data["Histories"]

    # Show
    print("\n--- Calculation Histories ---")

    if len(histories) == 0 :
        print("~~ No history ~~")
    else :
        for i in range(len(histories)) :
            print(histories[i])

    print(f"-----------------------------\nSave History? = {Data["SaveHistories"]}\n-----------------------------")

    # Del?
    AddOn = input("\n")

    if AddOn == "-" : # Clear History
        if input("\nAre you sure you want to clear histories? [y/n]\n= ").lower() == "y" :
            Data["Histories"] = []

            time.sleep(SLEEP_TIME)
            
            print("\nHistories cleared.\n\n")
        else :
            print("\n\n")
    elif AddOn == "0" : # Toggle History
        State = Data["SaveHistories"]
        WillState = not Data["SaveHistories"]

        Data["SaveHistories"] = not Data["SaveHistories"]

        time.sleep(SLEEP_TIME)

        print(f"\n{State} -> {WillState}\n\n")



def Run(HistoriesFile, Data) :
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
            HistoriesFile.save(Data)

            time.sleep(CLOSE_TIME)

            break
        elif Input in ("what's new", "whats new") :
            WhatNew()
        
        ## For Error
        else :
            print("\nInvalid command.\n\n")

# Code
DataFile = DataHandler("All Data.json")
Data = DataFile.DoFirst(Data)

Run(DataFile, Data)