from math import ceil
import numpy as py
import matplotlib as mpl

#Wszystkie zmienne dane które podawane będą z klawiatury:
#Temperatura ciała i temperatura wody (początkowe)
Tc = 0
Tw = 0
To = 0
#masa ciała i objętość wody
m = 0
V = 0
#cieplo wlasciwe ciala
Cc = 0

#stałe wartosci:
#gestosc wody
rho = 1 #kg/m^3
#cieplo wlasciwe wody
Cw = 4200 #J/kgK

def termometr(temkoncowa):
    if temkoncowa > 275.15 and temkoncowa < 375.15:
        return 0
    elif temkoncowa > 375.15:
        return 1
    else:
        return 2

print("Podaj dane dla ciala:")
while True:
    try:
        print("temperatura poczatkowa [K]:")
        Tc = float(input())
    except ValueError:
        print("Podaj wielkość liczbową")
        continue
    else:
        break
while True:
    try:
        print("masa [kg]:")
        m = float(input())
    except ValueError:
        print("Podaj wielkość liczbową")
        continue
    else:
        break
while True:
    try:
        print("cieplo wlasciwe [ J/kgK]:")
        Cc = float(input())
    except ValueError:
        print("Podaj wielkość liczbową")
        continue
    else:
        break

print("Podaj dane dla basenu:")
while True:
    try:
        print("temperatura poczatkowa [K]:")
        Tw = float(input())
    except ValueError:
        print("Podaj wielkość liczbową")
        continue
    else:
        break
while True:
    try:
        print("objetosc [m^3]:")
        V = float(input())
    except ValueError:
        print("Podaj wielkość liczbową")
        continue
    else:
        break

if Tw > Tc:
    dQ = (Tw - Tc)*(rho*V*m*Cw*Cc)/(m*Cc + rho * V * Cw)
    To = (-dQ)/(rho*V*Cw)+Tw
    dS = dQ*(Tw-Tc)/(Tc*Tw)
    print(dQ, To, dS)

if Tw < Tc:
    dQ = (Tc - Tw)*(rho*V*m*Cw*Cc)/(m*Cc + rho * V * Cw)
    To = (dQ)/(rho*V*Cw)+Tw
    dS = dQ*(Tc-Tw)/(Tc*Tw)
    print(round(dQ, 2), round(To, 2), round(dS, 2))

if termometr(To) == 1:
    V = ((m*Cc)/(rho*Cw))*((Tc-Tw)/(375.15 - Tw) - 1)
    print("Woda zaczyna wrzec, masz za mala objetosc basenu! Minimalna wielkosc basenu to: ", ceil(V))
elif termometr(To) == 2:
    V = ((m*Cc)/(rho*Cw))*((Tc-Tw)/(275.15 - Tw) - 1)
    print("
