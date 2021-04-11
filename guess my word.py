name = "python"
name = name.upper()
count = 3
user = []
for i in range(len(name)):
    user.append('-')
correct = 0
while(True):
    for i in user:
        print(i, end=' ')
    x = input('\nENTER THE AlPHA   ').upper() 
    if x in name:
        for id, value in enumerate(name): 
            if value == x:
                user[id] = x   
                correct += 1 
    else:
        print("WRONG GUESS")
        count = count - 1
        print(f'NOW YOU HAVE {count} lifeline')
    if count == 0:
        print("YOU LOOSED")
        break   
    if correct == len(name):
        print("great play,Hurray! You Won...")
        print(name)
        break    
