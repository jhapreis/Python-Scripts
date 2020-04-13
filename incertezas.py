from uncertainties import ufloat
from uncertainties.umath import *  # sin(), etc.

#para instalar essa biblioteca, vá nesse link: https://bootstrap.pypa.io/get-pip.py (ou mais atual)
#copie o texto do link, cole num bloco de notas e salve como um arquivo .py (ex.:get-pip.py)
#execute o script no terminal e você terá instalado o 'instalador de pacotes' do python.
#depois, rode esse comando  ' pip install --upgrade uncertainties ' e pronto, instalada.

x = ufloat(1, 0.1)  # x = 1+/-0.1

print (2*x)

print ( sin(2*x) )

print ( (2*x+1000).derivatives[x] )  