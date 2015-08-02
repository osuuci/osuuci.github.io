input = open("index.html", "r")

text = input.read()
text = text.replace('mauler68">mauler68', 'TheWeirdo9">TheWeirdo9')

output = open("index2.html", "w")
output.write(text)
