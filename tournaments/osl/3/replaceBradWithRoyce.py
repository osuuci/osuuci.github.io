input = open("index.html", 'r')
txt = input.read()

txt = txt.replace('/u/mauler68">mauler68', '/u/theweirdo9">TheWeirdo9')

output = open("output.html", 'w')
output.write(txt)
