
import win32api, time, win32con


def mover(x,y):
    win32api.SetCursorPos((x,y))
 

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

print("               .,-:;//;:=,                    ")
print("          . :H@@@MM@M#H/.,+%;,            ")
print("       ,/X+ +M@@M@MM%=,-%HMMM@X/,        ")
print("     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-       ")
print("    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.     ")
print("  ,%MM@@MH ,@%=             .---=-=:=,.    ")
print("  =@#@@@MX.,                -%HX$$%%%:;     ")
print(" =-./@M@M$                   .;@MMMM@MM:    ")
print(" X@/ -$MM/                    . +MM@@@M$    ")
print(",@M@H: :@:        MOUSE        . =X#@@@@-    ")
print(",@@@MMX, .         BY         /H- ;@M@M=    ")
print(".H@@@@M@+,         SALVIO      %MM+..%#$.    ")
print(" /MMMM@MMH/.                  XM@MH; =;    ")
print("  /%+%$XHH@$=              , .H@@@@MX,    ")
print("   .=--------.           -%H.,@@@@@MX,    ")
print("   .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.    ")
print("     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=    ")
print("       =%@M@M#@$-.=$@MM@@@M; %M%=    ")
print("         ,:+$+-,/H#MMMMMMM@= =,    ")
print("               =++%%%%+/:-.    ")
print("")
print("presione 1 para mover ")
print("presione 2 para clickear")
eleccion=int(input())


if(eleccion==1):

    atr = input("cuantas veces ")
    atr2 = input("cada cuanto ")
    numero=int(atr)
    numero2=float(atr2)
    neri=0

    while neri < numero:
        mover(100,100)
        neri=neri+1
        time.sleep(numero2)
        mover(200,200)
        
if(eleccion==2):
    input("apoye el mouse donde va a clikear y presione enter")
    x1, y1 = win32api.GetCursorPos()
    
    atr = input("cuantas veces ")
    atr2 = input("cada cuanto (vale float) ")
    numero=int(atr)
    numero2=float(atr2)
    neri=0

    while neri < numero:
        click(x1,y1)
        neri=neri+1
        time.sleep(numero2)
    
    
    
#print("fin")
input("fin")