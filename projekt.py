import sympy as sy

#Wszystkie zmienne dane które podawane będą z klawiatury:
#Temperatura ciała i temperatura wody (początkowe)
Tc, Tw = sy.symbols('Tc Tw')
#masa ciała i objętość wody
m, V = sy.symbols('m V')
#cieplo wlasciwe ciala
Cc = sy.symbols('Cc')

#stałe wartosci:
#gestosc wody
rho = 1 #kg/m^3
#cieplo wlasciwe wody
Cw = 4200 #J/kgK

if Tw > Tc:
    dQ = (Tc - Tw)*(rho*V*m*Cw*Cc)/(m*Cc + rho * V * Cw)
    To = dQ/(rho*V*Cw)+Tw
    dS = dQ*(Tc-Tw)/(Tc*Tw)

if Tw < Tc:
    dQ = (Tw - Tc)*(rho*V*m*Cw*Cc)/(m*Cc + rho * V * Cw)
    To = (-dQ)/(rho*V*Cw)+Tw
    dS = dQ*(Tw-Tc)/(Tc*Tw)
