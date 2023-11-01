
a= int(input("Vurma (1) , Çıxma 2() , Toplama (3) , Bölmə (4), Riyazi emeli daxil edin: "))

b=int(input("Eded daxil edin: "))

c=int(input("Eded daxil edin: "))




def MathFunc(a,b,c):
    if a==1:
        d = b*c
        print(f"Cavab : {b} * {c} = {d}")
    elif a==2:
        d = b-c
        print(f"Cavab : {b} - {c} = {d}")
    elif a==3:
        d = b+c
        print(f"Cavab : {b} + {c} = {d}")
    elif a==4:
        if c==0:
            print("0-a bolmek mumkun deyil!")
        else:
            d = b/c
        print(f"Cavab : {b} : {c} = {d}")

        

MathFunc(a,b,c)