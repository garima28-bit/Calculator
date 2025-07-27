import functions

a = int(input())
b = int(input())

op = input()

if op == "+":
    print(functions.add(a,b))
if op == "-":
    print(functions.sub(a,b))
if op == "*":
    print(functions.mul(a,b))
if op == "/":
    print(functions.div(a,b))
if op == "^":
    print(functions.power(a,b))
