<<<<<<< HEAD
x=int(input("Enter (1) for encryption and (2) for decryption: "))
e=int(input("Enter e: "))
n=int(input("Enter n: "))

if x==1:
    m= int(input("Enter message: "))
    ciper= (m**e)%n
    print(f"The encryption of {m} is = {ciper}")    

elif x==2:
     c= int(input("Enter ciper: ")) 
     def is_prime(num):
        if num==1:
            return True
        else:
            for i in range(2,num):
                if num%i==0:
                    return False
            return True  
        
     for p in range(2, n):
        if n % p == 0:
            q = n // p
            if is_prime(p) and is_prime(q):
                print(f"p={p}, q={q} are primes.")
                break
                 
     fie= (p-1)*(q-1)
     print(f"the fie ={fie}")
     
     for k in range(1,e+1):
         d= (1+ k*fie)/e
         if d==int(d):
             print(f"d = {d}")
             break
         
     message= (c**d)%n
     print(f"The decryption of {c} is = {message}")    
                 
else:
    print("Please enter correct option")    
    
    
    
=======
x=int(input("Enter (1) for encryption and (2) for decryption: "))
e=int(input("Enter e: "))
n=int(input("Enter n: "))

if x==1:
    m= int(input("Enter message: "))
    ciper= (m**e)%n
    print(f"The encryption of {m} is = {ciper}")    

elif x==2:
     c= int(input("Enter ciper: ")) 
     def is_prime(num):
        if num==1:
            return True
        else:
            for i in range(2,num):
                if num%i==0:
                    return False
            return True  
        
     for p in range(2, n):
        if n % p == 0:
            q = n // p
            if is_prime(p) and is_prime(q):
                print(f"p={p}, q={q} are primes.")
                break
                 
     fie= (p-1)*(q-1)
     print(f"the fie ={fie}")
     
     for k in range(1,e+1):
         d= (1+ k*fie)/e
         if d==int(d):
             print(f"d = {d}")
             break
         
     message= (c**d)%n
     print(f"The decryption of {c} is = {message}")    
                 
else:
    print("Please enter correct option")    
    
    
    
>>>>>>> 1912e7ac5f445a6a3782e866f177253e182f6826
  