file = open('class_notes.txt', 'r')
for line in file:
    print(line.strip())
file.close()

with open('class_notes.txt', 'r') as f:
    for line in f:
        print(line.strip())