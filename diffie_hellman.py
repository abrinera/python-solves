p=int(input("Enter p: "))
g=int(input("Enter g: "))
a=int(input("Gojo sensei enter your key(a): "))
b=int(input("Geto sama enter your key(b):"))

A=(g**a)%p

B=(g**b)%p

#Gojo's shared key
sa=(B**a)%p

#Geto's shared key
sb=(A**b)%p

if sa==sb and sa!=1:
    print(f"Shared key is: {sa}")
else:
    print("************|Domain Expansion, Malevolent  Kitchen|************")    