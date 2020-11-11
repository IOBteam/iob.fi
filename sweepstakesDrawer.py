import random

second = [2, 3, 4, 5, 6]
third = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

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
        if count == 1:
            print('--- First Place ---')
            print(f'1. {winner}')
            winnersAddy.append(winner)
            addy.remove(winner)
            Winners.write(winner + '\n')
            count += 1
        elif count in second:
            if count == 2:
                print('--- Second Place ---')
            print(f"{count}. {winner}")
            winnersAddy.append(winner)
            addy.remove(winner)
            Winners.write(winner + '\n')
            count += 1
        elif count in third:
            if count == 7:
                print('--- Third Place ---')
            print(f"{count}. {winner}")
            winnersAddy.append(winner)
            addy.remove(winner)
            Winners.write(winner + '\n')
            count += 1

Winners.close()

print('Finished Drawing 1st 16 winners...')
input('Press enter to draw second drawing.')

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
        if count == 1:
            print('--- First Place ---')
            print(f'1. {winner}')
            winnersAddy.append(winner)
            addy.remove(winner)
            Winners.write(winner + '\n')
            count += 1
        elif count in second:
            if count == 2:
                print('--- Second Place ---')
            print(f"{count}. {winner}")
            winnersAddy.append(winner)
            addy.remove(winner)
            Winners.write(winner + '\n')
            count += 1
        elif count in third:
            if count == 7:
                print('--- Third Place ---')
            print(f"{count}. {winner}")
            winnersAddy.append(winner)
            addy.remove(winner)
            Winners.write(winner + '\n')
            count += 1

Winners.close()

print('Finished Drawing 2nd 16 winners...')
input('Press enter to draw third drawing.')

addresses = open("Token Request Qualified.txt", 'r')
addy = addresses.readlines()
addy = [x.strip() for x in addy]
addresses.close()
Winners = open('Winners #3.txt', 'a')


print(f"There are a total of {len(addy)} participants.")
print('Drawing 3rd 16 winners...')

count = 1

for a in addy:
    if not count < 17:
        break
    else:
        winner = addy[random.randint(0, len(addy) - count)]
        if winner in winnersAddy:
            continue
        if count == 1:
            print('--- First Place ---')
            print(f'1. {winner}')
            winnersAddy.append(winner)
            addy.remove(winner)
            Winners.write(winner + '\n')
            count += 1
        elif count in second:
            if count == 2:
                print('--- Second Place ---')
            print(f"{count}. {winner}")
            winnersAddy.append(winner)
            addy.remove(winner)
            Winners.write(winner + '\n')
            count += 1
        elif count in third:
            if count == 7:
                print('--- Third Place ---')
            print(f"{count}. {winner}")
            winnersAddy.append(winner)
            addy.remove(winner)
            Winners.write(winner + '\n')
            count += 1

Winners.close()

print('Finished Drawing 3rd 16 winners...')
