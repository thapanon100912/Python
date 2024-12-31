# Calculator.py
# Version 10.0
VERSION = "10.0"

# Import things
import time
import math

# Configs
VERSION_MESSAGE = "Version {version} : What's new".format(version = VERSION)
SLEEP_TIME = 1
CLOSE_TIME = 4
VALUEERROR = "Unknown Value: Please Type Again"
ZERODIVISIONERROR = "Have Something Error: Cann't divided by 0"

# Operator Functions
def Plus() :
    try :
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
            
            finally :
                pass
        
        # Calculate
        Answer = a + b
        
        #Float -> Int
        if Answer == int(Answer) :
            Answer = int(Answer)

        time.sleep(SLEEP_TIME)
        print ("Answer =" , Answer ,"\n\n")
    
    except Exception as Reason :
        print("Have Something Error :" , Reason)

def Minus() :
    try :
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
            
            finally :
                pass
        
        # Calculate
        Answer = a - b

        #Float -> Int
        if Answer == int(Answer) :
            Answer = int(Answer)

        time.sleep(SLEEP_TIME)
        print ("Answer =" , Answer ,"\n\n")
    
    except Exception as Reason :
        print("Have Something Error :" , Reason)

def Times() :
    try :
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
            
            finally :
                pass
        
        # Calculate
        Answer = a * b
        
        #Float -> Int
        if Answer == int(Answer) :
            Answer = int(Answer)

        time.sleep(SLEEP_TIME)
        print ("Answer =" , Answer ,"\n\n")

    except Exception as Reason :
        print("Have Something Error :" , Reason)

def Divide() :
    try :
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
            
            finally :
                pass
        
        # Calculate
        Answer = int(a // b)
        Remander = int(a % b)
        Answer_WithDecemal = a / b
        
        #Float -> Int
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

    except ZeroDivisionError :
        print(ZERODIVISIONERROR)
    except Exception as Reason :
        print("Have Something Error:" , Reason)

def Power() :
    try :
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
            
            finally :
                pass
        
        # Calculate
        Answer = a ** b
        
        #Float -> Int
        if Answer == int(Answer) :
            Answer = int(Answer)

        time.sleep(SLEEP_TIME)
        print ("Answer =" , Answer ,"\n\n")

    except Exception as Reason :
        print("Have Something Error :" , Reason)

def Root() :
    try :
        # Ask
        while True :
            try :
                print("\n")

                #Ask A
                a = input("Sqr, Cqr = ")

                #Check A -> Sqr = True, Cqr = False
                if a == "Sqrt" or a == "1":
                    a = "Sqrt"
                elif a == "Cbrt" or a == "2" :
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

            finally :
                pass
        
        # Calculate
        if a == "Sqrt" :
            Answer = math.sqrt(b)
        if a == "Cbrt" :
            Answer = math.cbrt(b)
        
        #Float -> Int
        if Answer == int(Answer) :
            Answer = int(Answer)

        time.sleep(SLEEP_TIME)
        print ("Answer =" , Answer ,"\n\n")

    except Exception as Reason :
        print("Have Something Error :" , Reason)

def Factorial() :
    try :
        # Ask
        while True :
            try :
                print("\n")

                #Ask A
                a = int(math.fabs(int(input("A = "))))
                print(a,"\n")
                break

            except ValueError :
                print(VALUEERROR)
            
            finally :
                pass
        
        # Calculate
        Answer = math.factorial(a)

        time.sleep(SLEEP_TIME)
        print ("Answer =" , Answer ,"\n\n")

    except Exception as Reason :
        print("Have Something Error :" , Reason)

# Functions
def WhatNew() :
    print(
          "1. Change Code Stucture",
        "\n2. Change Some Feature", "\n\n"
    )

def Move() :
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def Run() :
    print(VERSION_MESSAGE)

    while True :
        Input = input("pl, mi, mu, di, ex, rt, !, move, leave\nInput = ") ## Guide

        ## Operations
        if Input == "pl" or Input == "Pl" :
            Plus()

        elif Input == "mi" or Input == "Mi" :
            Minus()

        elif Input == "mu" or Input == "Mu" :
            Times()

        elif Input == "di" or Input == "Di" :
            Divide()

        elif Input == "ex" or Input == "Ex" :
            Power()

        elif Input == "rt" or Input == "Rt" :
            Root()
        
        elif Input == "!" :
            Factorial()
        
        ## Functions
        elif Input == "move" or Input == "Move" :
            time.sleep(SLEEP_TIME)

        elif Input == "leave" or Input == "Leave" :
            time.sleep(CLOSE_TIME)

            break
        elif Input == "What's new" or Input == "whats new" :
            WhatNew()
        
        ## For Error
        else :
            print("\nError\n\n")

# Code
Run()