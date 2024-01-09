def divisors(integer):
    num = []
    for i in range(integer):
        
        if i == 0 or i == 1:
           continue 
        if integer%i == 0:
            num.append(i)
    if len(num) == 0:
        string = str(integer)+' is prime'
        return string
    else:
        return num

        
    
    pass

    

divisors(12)
print(divisors(17))