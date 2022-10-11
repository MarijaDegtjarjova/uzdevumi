2 stunda

#if else
sk1=101
if sk1<100:
 print("skaitlis mazs")
 print("AAAAA,cik liels skaitlis")
else:
 print("skaitlis ir liels")




#lists - saraksti []
sar1=[1,2,3,4,5]
sar2=["diena","nakts","sesija"]
sar3=sar1+sar2
sar3.append("Hello")
sar3.insert(5,"Sveiki")
print(sar3)



vecums=int(input("cik tev gadu?"))
if vecums<18:
  print("Ej macities!")
else:
  print("Ej uz darbu!")



abc=56
sk1=int(input("Īevadi skaitli"))
if sk1%2==0:
  print("Para skaitlis")
else:
  print("nepāra skaitlis") 




teksts=input("Īevadi kaut kadu teksti")
#indeki 
#OKTOBRIS -> 8
print(teksts[2:5])


teksts=input("Īevadi kaut kadu teksti")
#indeki 
#OKTOBRIS -> 8
print(teksts[2],teksts[5])






#lists - saraksti []
sar1=[1,2,3,4,5]
sar2=["sveiki","paldies","ludzu"]
sar3=sar1+sar2
sar3.insert
sar3.pop(5)
print(sar3)


sk1=int(input("Ievadiet skaitli: "))
if sk1>10:
  print("Skaitlis ir liels")
else:
  print("Skaitlis ir mazs")




from math import *
a=int(input("ievaditiet a: "))
b=int(input("ievaditiet b: "))
c=int(input("ievaditiet c: "))
D=b**2-4*a*c
if D<0:
  print("sakņu nav!")
elif D==0:
  x=-b/2*a
  print("Ir viena sakne=",x)
else:
  x1=(-b+sqrt(D))/2*a
  x2=(-b+sqrt(D))/2*a
  print("ir divas saknes, x1=",x1," x2 =",x2)
