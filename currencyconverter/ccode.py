from locale import currency
from cgitb import reset
from unittest import result
from unittest import result
from forex_python.converter import currency
curr=CurrencyRates()

amount=float(input("enter number"))
from_c=input("from currency: ").upper()
to_c=input("to currency:").upper()

result=curr.convert(from_c,to_c,amount)

print(f"{amount},{from_c}={result},{to_c}")





