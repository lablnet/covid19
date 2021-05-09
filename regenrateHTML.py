from random import randrange

ts = str(randrange(1000, 99999))

file = "./web/public/index.html"
content = ""
with open(file, "r") as fh:
    content = fh.read()

index = 0
html = ""
print(ts)
for chars in content:
    html += chars
    if chars == "j" and content[index + 1] == "s":
        gif html[:16] == "<!--modified-->\n":
            print("tesr")
            html = html[: -10]
            print("Test", html)

        html += "s?v="+ ts
    index = index + 1

html = "<!--modified-->\n" + html
print(html[:16])
print(html[:16] == "<!--modified-->\n")
# print(html)
# with open(file, "w") as fh:
#     fh.write(html)
