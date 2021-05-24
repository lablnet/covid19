from random import randrange


def getRand():
    return str(randrange(10000, 99999))


file = "./web/public/index.html"
content = ""
with open(file, "r") as fh:
    content = fh.read()


index = 0
html = ""
iterator = -1
for chars in content:
    html += chars
    if iterator == 9:
        # Reset iterator and delete previous ?v= append versions value
        iterator = -1
        html = html[: -9]
    if chars == "j" and content[index + 1] == "s":
        if html[:16] == "<!--modified-->\n":
            html += "s?v="+ getRand()
            iterator = 0
    index = index + 1

    # To ensure to iterate only if found
    if iterator >= 0:
        iterator += 1

with open(file, "w") as fh:
    fh.write(html)

# Finally, Done.
print("Done, Thanks")
