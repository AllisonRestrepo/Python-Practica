import math
a1 = ((2+7)**3 + 273**(2/3)/2 + 55**2/3)
b1 = 43 * (250 **(1/4)+23)**2/math.exp(45-3**3)
c1 = math.cos(((5*math.pi)/6)**2)*(math.sin((7*math.pi)/8))**2+(math.tan(((math.pi)/6)*math.log(8)))/(7*(5/2))
x = 9.6
d1 =math.log10(abs(x**2 - x**3))
a = 15
b = -7.08
c = 62.5
d = 0.5 * (a*b-c)
e1 =d* math.exp(d/2) + (a*d+c*d)/(20/a + 30/b)/(a+b+c+d)
alpha = 5 * math.pi /9
beta = math.pi /7
iz = math.cos(alpha)-math.cos(beta)
der = 2* math.sin((alpha+beta)/(2))*math.sin((beta - alpha)/(2))

print(f"""
---------RESULTADOS------------
resultado a: {a1}
resultado b: {b1}
resultado c: {c1}
resultado d: {d1}
resultado e: {e1}
-----RESULTADOS IZ Y DER ------
resultado iz: {iz}
resultado der: {der}""")