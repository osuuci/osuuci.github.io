import urllib2
from bs4 import BeautifulSoup
import random

file = open('test.txt', 'r')
soup = BeautifulSoup(file)

# print soup.prettify()

matchLetters = []
for anchor in soup.find_all('a'):
    if 'class' in anchor.attrs:
        if 'match_identifier' in anchor['class']:
            matchLetters.append(anchor.get_text().strip())

players = []
            
for div in soup.find_all('div'):
    if 'class' in div.attrs:
        if 'participant-present' in div['class']:
            players.append(div.span.get_text())

matches = []

for index in range(len(matchLetters)):
    player1 = index * 2
    player2 = index * 2 + 1
    matches.append((matchLetters[index], (players[player1], players[player2])))

randomMatches = []
while len(matches) > 0:
    randomMatches.append(matches.pop(random.randint(0, len(matches) - 1)))

output = open('output.html', 'w')

def wl(file, string):
    file.write(string + "\n")

wl(output, '<table>')
    
starttime = 7.5 * 60
    
for index in range(len(randomMatches)):
    if index % 4 == 0:
        starttime = starttime + 30
    if index % 16 == 0:
        starttime = 8 * 60
    wl(output, "<tr>")
    wl(output, "<td>")
    wl(output, "OSL" + str(index + 1))
    wl(output, "</td>")
    wl(output, "<td>")
    day = "Sat "
    if index >= 16:
        day = "Sun "
    
    if starttime % 60 == 0:
        wl(output, day + str(int(starttime/60)) + ":00 PM")
    else:
        wl(output, day + str(int(starttime/60)) + ":30 PM")
    wl(output, "</td>")
    wl(output, "<td>")
    wl(output, randomMatches[index][1][0])
    wl(output, "</td>")
    wl(output, "<td>")
    wl(output, randomMatches[index][1][1])
    wl(output, "</td>")

    wl(output, "<td>")
    wl(output, "N/A")
    wl(output, "</td>")

    wl(output, "<td>")
    wl(output, "N/A")
    wl(output, "</td>")

    wl(output, "<td>")
    if index % 4 == 0:
        wl(output, '<a href="https://osu.ppy.sh/u/1472763">osuuci dot com</a>')
    elif index % 4 == 1:
        wl(output, '<a href="https://osu.ppy.sh/u/shintomo">Shintomo</a>')
    elif index % 4 == 2:
        wl(output, '<a href="https://osu.ppy.sh/u/mauler68">mauler68</a>')
    elif index % 4 == 3:
        wl(output, '<a href="https://osu.ppy.sh/u/lalipo">lalipo</a>')
    wl(output, "</td>")
    wl(output, "</tr>")

wl(output, "</table>")
