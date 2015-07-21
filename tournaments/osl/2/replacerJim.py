inputFile = open("index.html", 'r')
txt = inputFile.read()

txt = txt.replace('href="https://osu.ppy.sh/u/1472763">osuuci dot com', 'href=https://osu.ppy.sh/u/Jim">Jim')


outputFile = open("output.html", 'w')
outputFile.write(txt)
outputFile.close()
