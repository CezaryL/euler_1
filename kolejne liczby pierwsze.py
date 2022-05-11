x=[2, 3, 5, 7, 11]



print(x)
z=12

while True:


    if len(x)>=10001: break
    print (z)
    for i in x:
        print(z,i,"!!",z%i)

        if z%i==0:
            test=True
            break

    if test==False:
        x.append(z)
        print("dodaje")
    z+=1
    test = False
print(x)