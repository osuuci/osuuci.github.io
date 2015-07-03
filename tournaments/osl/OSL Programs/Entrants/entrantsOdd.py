odd = open("odd.txt", "w")

with open('entrants.csv', 'r') as entrants:
    counter = 0
    for line in entrants:
        split = line.split(',')
        counter = counter + 1
        if counter % 2 == 0:
            print split[1]
            odd.write(split[1] + "\n")
