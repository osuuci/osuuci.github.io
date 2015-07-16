index = open("index - Copy.html", "r")

text = index.read()
text = text.replace(" PM", "PM")

output = open("index.html", "w")
output.write(text)
