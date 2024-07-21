#เครื่องคิดเลข
#V.9.6
#fuc
import time
def pl() : #pl
    try:
        TT = int(input('setter : '))
        print (TT)
        TT2 = (int(input('adder : ')))
        print (TT2)
        ansTT = TT+TT2
        print('wait...')
        time.sleep(1)
        print ('\nanswer : ' , ansTT ,"\n\n")
    except:
        print('[ERROR]')
    finally:
        pass
def pldot() : #pl.
    try:
        TTf = float(input('setter : '))
        print (TTf)
        TTf2 = (float(input('adder : ')))
        print (TTf2)
        ansTTf = TTf+TTf2
        print('wait...')
        time.sleep(1)
        print ('\nanswer : ' , ansTTf ,"\n\n")
    except:
        print('[ERROR]')
    finally:
        pass
def mi() : #mi
    try:
        MMf = int(input('setter : '))
        print (MMf)
        MMf2 = (int(input('subtrahend : ')))
        print (MMf2)
        ansMMf = MMf-MMf2
        print('wait...')
        time.sleep(1)
        print ('\nanswer : ' , ansMMf ,"\n\n")
    except:
        print('[ERROR]')
    finally:
        pass
def midot() : #mi.
    try:
        MMf = float(input('setter : '))
        print (MMf)
        MMf2 = (float(input('subtrahend : ')))
        print (MMf2)
        ansMMf = MMf-MMf2
        print('wait...')
        time.sleep(1)
        print ('\nanswer : ' , ansMMf ,"\n\n")
    except:
        print('[ERROR]')
    finally:
        pass
def mu() :#mu
    try:
        T = int(input('setter : '))
        print (T)
        T2 = (int(input('Multiplier : ')))
        print (T)
        ansT = T*T2
        print('wait...')
        time.sleep(1)
        print ('\nanswer : ' , ansT ,"\n\n")
    except:
        print('[ERROR]')
    finally:
        pass
def mudot () : #mu.
    try:
        Tf = float(input('setter : '))
        print (Tf)
        Tf2 = (float(input('Multiplier : ')))
        print (Tf)
        ansTf = Tf * Tf2
        print('wait...')
        time.sleep(1)
        print ('\nanswer : ' , ansTf ,"\n\n")
    except:
        print('[ERROR]')
    finally:
        pass
def di() : #di
    try:
        M = int(input('setter : '))
        print (M)
        M2 = (int(input('divisor : ')))
        print (M2)
        ansMnoDOT = (M//M2)
        ansMD0T = M/M2
        ansMnoDOTss = M % M2
        print('wait...')
        time.sleep(2)
        print ('\nanswer : ' , ansMnoDOT)
        print ('//' , ansMnoDOTss ,"\n\n")
    except:
        print('[ERROR]')
    finally:
        pass
def didot() : #di.
    try:
        Mf = float(input('setter : '))
        print (Mf)
        Mf2 = (float(input('divisor : ')))
        print (Mf2)
        ansMfD0T = Mf/Mf2
        ansMfnoDOTss = Mf % Mf2
        print('wait...')
        time.sleep(2)
        print ('\nanswer : ' , ansMfD0T)
        print ('// = ' , ansMfnoDOTss ,"\n\n")
    except:
        print('[ERROR]')
    finally:
        pass
def ex() : #ex
    try:
        ex = int(input('setter : '))
        print (ex)
        ex2 = (int(input('exalt : ')))
        print (ex2)
        ansex = int(ex**ex2)
        print('wait...')
        time.sleep(1)
        print ('\nanswer : ' , ansex ,"\n\n")
    except:
        print('[ERROR]')
    finally:
        pass
def exdot() : #exdot
    try:
        exf = float(input('setter : '))
        print (exf)
        exf2 = (float(input('exalt : ')))
        print (exf2)
        ansexf = float(exf**exf2)
        print('wait...')
        time.sleep(1)
        print ('\nanswer : ' , ansexf ,"\n\n")
    except:
        print('[ERROR]')
    finally:
        pass
def fac() : #!
    try:
        import math
        fac = int(input('! : '))
        print (fac)
        ansfac = math.factorial(fac)
        print('wait...')
        time.sleep(1)
        print ('\nanswer : ' , ansfac ,"\n\n")
    except:
        print('[ERROR]')
    finally:
        pass
'''
def ploo(*ploo) :
    while True :
        str(ploo2)
        ploo2 = input('If you want to stop typing, stop : ')
        if ploo2 == 'stop' :
            ploo += ploo2
            break
        else :
            float(ploo2)
            ploo += ploo2
'''
#go
print('starting calculator.....')
time.sleep(3)
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print ('V.9.6\twhat new')
while True :
    Home = input("pl mi mu di ex *. ! ms1 ms2 leave : ")
    if Home =='pl' :
        pl()
    elif Home =='pl.' :
        pldot()
    #elif Home == 'plinv' :
            #plinv = input('If you want to stop typing, stop : ')
            #ploo(plinv)
    elif Home == 'mi' :
        mi()
    elif Home == 'mi.' :
        midot()
    elif Home =='mu' :
        mu()
    elif Home =='mu.' :
        mudot()
    elif Home =='di' :
        di()
    elif Home =='di.' :
        didot()
    elif Home =='ex' :
        ex()
    elif Home =='ex.' :
        exdot()
    elif Home =='!' :
        fac()
    elif Home == 'ms1' :
        mol = int(input('put number 1 : '))
        print (mol)
        mol2 = (int(input('put number 2 : ')))
        print (mol2)
        print('wait...')
        time.sleep(1)
        if mol > mol2 :
            print ('answer : >')
        elif mol < mol2 :
            print ('answer : <')
        elif mol == mol2 :
            print ('answer : =')
    elif Home == 'ms2' :
        print ('!!!!This function may confuse you')
        Homein = input('pl mi mu *. di ex : ')
        if Homein == 'pl' :
            TTin = int(input('-- : '))
            TT2in = int(input('-- : '))
        elif Homein =='pl.' :
            TTfin = float(input('setter : '))
            print (TTfin)
            TTf2in = (float(input('adder : ')))
            print (TTf2in)
            ansin = TTfin+TTf2in
            print (ansin)
        elif Homein == 'mi' :
            MMin = int(input('-- : '))
            MM2in = int(input('-- : '))
            ansin = MMin - MM2in
            print (ansin)
        elif Homein == 'mi.' :
            MMfin = float(input('setter : '))
            print (MMfin)
            MMf2in = (float(input('subtrahend : ')))
            print (MMf2in)
            ansin = MMfin-MMf2in
            print (ansin)
        elif Homein == 'mu' :
            Tin = int(input('-- : '))
            T2in = int(input('-- : '))
            ansin = Tin * T2in
            print (ansin)
        elif Homein =='mu.' :
            Tfin = float(input('setter : '))
            print (Tfin)
            Tf2in = (float(input('Multiplier : ')))
            print (Tf2in)
            ansin = Tfin*Tf2in
            print (ansin)
        elif Homein == 'di' :
            Min = float(input('-- : '))
            M2in = float(input('-- : '))
            ansin = Min / M2in
            print (ansin)
        elif Homein == 'ex' :
            exin = int(input('-- : '))
            ex2in = int(input('-- : '))
            ansin = exin ** ex2in
            print (ansin)
        Homein2 = input('pl mi mu *. di ex : ')
        if Homein2 == 'pl' :
            TTin2 = int(input('-- : '))
            TT2in2 = int(input('-- : '))
            ansin2 = TTin2 + TT2in2
            print (ansin2)
        elif Homein2 =='pl.' :
            TTfin2 = float(input('setter : '))
            print (TTfin2)
            TTf2in2 = (float(input('adder : ')))
            print (TTf2in2)
            ansin = TTfin2+TTf2in2
            print (ansin)
        elif Homein2 == 'mi' :
            MMin2 = int(input('-- : '))
            MM2in2 = int(input('-- : '))
            ansin2 = MMin2 - MM2in2
            print (ansin2)
        elif Homein2 == 'mi.' :
            MMfin2 = float(input('setter : '))
            print (MMfin2)
            MMf2in2 = (float(input('subtrahend : ')))
            print (MMf2in2)
            ansin2 = MMf2in2-MMfin2
            print (ansin2)
        elif Homein2 == 'mu' :
            Tin2 = int(input('-- : '))
            T2in2 = int(input('-- : '))
            ansin2 = Tin2 * T2in2
            print (ansin2)
        elif Homein2 =='mu.' :
            Tfin2 = float(input('setter : '))
            print (Tfin2)
            Tf2in2 = (float(input('Multiplier : ')))
            print (Tfin2)
            ansin2 = Tfin2 * Tf2in2
            print (ansin2)
        elif Homein == 'di' :
            Min2 = int(input('-- : '))
            M2in2 = int(input('-- : '))
            ansin2 = Min2 / M2in2
            print (ansin2)
        elif Homein == 'ex' :
            exin2 = int(input('-- : '))
            ex2in2 = int(input('-- : '))
            ansin2 = exin ** ex2in2
            print (ansin2)
        if ansin > ansin2 :
            print ('answer : >')
        elif ansin < ansin2 :
            print ('answer : <')
        elif ansin == ansin2 :
            print ('answer : =')
    elif Home == 'what new' :
        print ('Programs that support only Thai language to see')
        print ('1.ทำให้ดูง่ายขึ้น')
    elif Home =='leave' :
        inle=input('do you want to shutting down? (YES , NO):\n')
        if inle == 'YES' :
            break
        else :
            pass
    else :
        print ('system error')
        pass
print ('shutting down......')
time.sleep(3)