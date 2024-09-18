pp = int(input("how many points are possible to get?: "))
pa = int(input("how many points did the student accieve?: "))
per = pa / pp
cent = per * 100
print("the student accieved " + str(cent) + "%")
if cent <= 50:
    print("F")
elif cent <=60:
    print("D")
elif cent <=75:
    print("C")
elif cent <=88:
    print("B")
elif cent <=100:
    print("A")
else:
    print("idfk")
