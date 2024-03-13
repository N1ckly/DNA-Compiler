import brainfuck as bf

f = open("main.dna", "r")
code = f.read().replace('-','').replace('\n','').replace(' ','')
f.close()

bfcode = ""

for i in range(0, len(code), 4):
    part = code[i:i+4]
    if part == "ATAT":
        bfcode += ">"
    if part == "ATGC":
        bfcode += "<"
    if part == "ATTA":
        bfcode += "+"
    if part == "ATCG":
        bfcode += "-"
    if part == "GCAT":
        bfcode += "."
    if part == "GCGC":
        bfcode += ","
    if part == "GCTA":
        bfcode += "["
    if part == "GCCG":
        bfcode += "]"

bf.evaluate(bfcode)
print()