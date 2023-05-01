from random import randint
numbers = []                          
i = 0
new_number = 0
while i < 4:  
    new_number = randint(0, 9)       
    if new_number not in numbers:     
        numbers.append(new_number)    
        i += 1
print('complete Create ramdom number.\n')
