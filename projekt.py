from math import ceil
import numpy as np
import matplotlib.pyplot as plt

#Wszystkie zmienne dane które podawane będą z klawiatury:
#Temperatura ciała i temperatura wody (początkowe)
Tc = 0
Tw = 0
#masa ciała i objętość wody
m = 0
V = 0
#cieplo wlasciwe ciala
Cc = 0

#stałe wartosci:
#gestosc wody
rho = 1000 #kg/m^3
#cieplo wlasciwe wody
Cw = 4200 #J/kgK

def termometr(temkoncowa):
    if temkoncowa >= 273.15 and temkoncowa <= 373.15:
        return 0
    elif temkoncowa > 373.15:
        return 1
    else:
        return 2

def CzyDobraObjetosc(To, m, Cc, Cw, Tc, Tw):
    if termometr(To) == 1:
        V = ((m * Cc) / (rho * Cw)) * ((Tc - Tw) / (373.15 - Tw) - 1)
        return print("Woda zaczyna wrzec, masz za mala objetosc basenu! Minimalna wielkosc basenu to: ", ceil(V), "m^3")
    elif termometr(To) == 2:
        V = ((m * Cc) / (rho * Cw)) * ((Tc - Tw) / (273.15 - Tw) - 1)
        return print("Woda zaczyna krzepnac, masz za mala objetosc basenu! Minimalna wielkosc basenu to: ", ceil(V), "m^3")
    else:
        return termometr(To)

def CzyLiczbaDobraInator(Zmienna):
    while True:
        try:
            Zmienna = float(Zmienna)
        except:
            print("Podaj liczbe:")
            Zmienna = CzyLiczbaDobraInator(input())
        else:
            Zmienna = float(Zmienna)
            break
    while Zmienna <= 0:
        print("Podaj poprawna wartosc:")
        Zmienna = CzyLiczbaDobraInator(input())
    return float(Zmienna)

def CzyDobraTemperatura(Zmienna):
    Zmienna = CzyLiczbaDobraInator(Zmienna)
    while Zmienna < 273.15 or Zmienna > 373.15:
        print("Woda nie ma odpowiedniej temperatury. Popraw:")
        Zmienna = CzyLiczbaDobraInator(input())
    return Zmienna

print("Podaj dane dla ciala:")
print("temperatura poczatkowa [K]:")
Tc = CzyLiczbaDobraInator(input())
print("masa [kg]:")
m = CzyLiczbaDobraInator(input())
print("cieplo wlasciwe [ J/kgK]:")
Cc = CzyLiczbaDobraInator(input())
print("Podaj dane dla basenu:")
print("temperatura poczatkowa [K]:")
Tw = CzyDobraTemperatura(input())
print("objetosc [m^3]:")
V = CzyLiczbaDobraInator(input())

if Tw > Tc:
    dQ = (Tw - Tc)*(rho*V*m*Cw*Cc)/(m*Cc + rho * V * Cw)
    To = (-dQ)/(rho*V*Cw)+Tw
    dS = m*Cc*np.log(abs(To/Tc), np.e) + rho*V*Cw*np.log(abs(To/Tw), np.e)
    if CzyDobraObjetosc(To, m, Cc, Cw, Tc, Tw) == 0:
        print("dQ[J] = ", round(dQ, 2), ",", "To[K] = ", round(To, 2), ",", "dS[J/K] = ", round(dS, 2))
        # Wykresy
        TemCialoX = np.linspace(Tc, To, 100)
        CieploCialoY = m * Cc * (TemCialoX - Tc)

        TemWodaX = np.linspace(Tw, To, 100)
        CieploWodaY = rho * V * Cw * (-TemWodaX + Tw)

if Tw < Tc:
    dQ = (Tc - Tw)*(rho*V*m*Cw*Cc)/(m*Cc + rho * V * Cw)
    To = (dQ)/(rho*V*Cw)+Tw
    dS = m*Cc*np.log(abs(To/Tc)) + rho*V*Cw*np.log(abs(To/Tw))
    if CzyDobraObjetosc(To, m, Cc, Cw, Tc, Tw) == 0:
        print("dQ[J] = ", round(dQ, 2), ",", "To[K] = ", round(To, 2), ",", "dS[J/K] = ", round(dS, 2))
        # Wykresy
        TemCialoX = np.linspace(Tc, To, 100)
        CieploCialoY = m * Cc * (-TemCialoX + Tc)

        TemWodaX = np.linspace(Tw, To, 100)
        CieploWodaY = rho * V * Cw * (TemWodaX - Tw)

plt.plot(TemCialoX, CieploCialoY, color='y', lw=1, ls='--', label='Qciala(T)')
plt.plot(TemWodaX, CieploWodaY, color='b', lw=1, ls='--', label='Qwody(T)')
plt.legend()
plt.xlabel('T[K]')
plt.ylabel('dQ[J]')
plt.title('Wykres funkcji przeplywu ciepla do temperatury Q(T):')
plt.grid(True)
plt.show()
#zmienilem wzory na entropie, zmienilem stale na poprawne
