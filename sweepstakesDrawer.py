import random

addresses = open("Drawing #1 Qualified.txt", 'r')
addy = addresses.readlines()
addy = [x.strip() for x in addy]
addresses.close()
Winners = open('Winners #1.txt', 'a')
winnersAddy = []

print(f"There are a total of {len(addy)} participants.")
print('Drawing 1st 16 winners...')

count = 1

for a in addy:
    if not count < 17:
        break
    else:
        winner = addy[random.randint(0, len(addy) - count)]
        winnersAddy.append(winner)
        addy.remove(winner)
        Winners.write(winner + '\n')
        count += 1
Winners.close()

print('Finished Drawing 1st 16 winners...')


addresses = open("Drawing #2 Qualified.txt", 'r')
addy = addresses.readlines()
addy = [x.strip() for x in addy]
addresses.close()
Winners = open('Winners #2.txt', 'a')

print(f"There are a total of {len(addy)} participants.")
print('Drawing 2nd 16 winners...')

count = 1

for a in addy:
    if not count < 17:
        break
    else:
        winner = addy[random.randint(0, len(addy) - count)]
        if winner in winnersAddy:
            continue
        else:
            winnersAddy.append(winner)
            addy.remove(winner)
            Winners.write(winner + '\n')
            count += 1
Winners.close()

print('Finished Drawing 2nd 16 winners...')