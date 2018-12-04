def zzs():
    I = 0
    while True:
        I += 1
        yield I
         
x = zzs()
 
for i in x:
     print (i)