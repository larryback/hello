sum = 0
for x in range(2,100):
    
    if x >2 and x%2 == 0:
        continue

    elif x > 3 and x%3 == 0:
        continue

    elif x > 5 and x%5 == 0:
        continue 

    elif x > 7 and x%7 == 0:
        continue 

    else:   
        sum = sum + x 
        

print(sum)