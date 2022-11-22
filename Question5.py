fin = open("poem.txt")

for line in fin:
    if line[0] == "A":
        print(line)
