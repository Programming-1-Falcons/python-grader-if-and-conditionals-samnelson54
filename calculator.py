

inone = str(input("what operator do you want?: "))
intwo = float(input("first number?: "))
inthree = float(input("second number?: "))


if inone == "+":
    solution = intwo + inthree
    print(str(intwo) + " " +str(inone) + " " + str(inthree) + " " + "= "+str(solution))
elif inone == "-":
    solution = intwo - inthree
    print(str(intwo) + " " +str(inone) + " " + str(inthree) + " " + "= "+str(solution))
elif inone == "*":
    solution = intwo * inthree
    print(str(intwo) + " " +str(inone) + " " + str(inthree) + " " + "= "+str(solution))
elif inone == "/":
    solution = intwo / inthree
    print(str(intwo) + " " +str(inone) + " " + str(inthree) + " " + "= "+str(solution))
elif inone == "**":
    solution = intwo ** inthree
    print(str(intwo) + " " +str(inone) + " " + str(inthree) + " " + "= "+str(solution))
else:
    print("invalid operator")