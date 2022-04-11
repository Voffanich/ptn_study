import random

phrase = input("Give the phrase! ")
steps = 0
done = False
attempt = ''
symbols = len(phrase)

while not done:
    
    for i in range(symbols):
        attempt = attempt + random.choice('abcdefghijklmnopqrstuvwxyz ')
    
    
    if attempt == phrase:
        done == True
        print(steps)
        break
    else:
        steps += 1
        attempt = ''
    
