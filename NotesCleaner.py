file = open('class_notes.txt', 'r')
n = int(input("Enter how many characters to preview: "))
print(file.read(n))
file.close()
file = open('class_notes.txt', 'r')
lines = file.readlines()
print('Total lines: ', len(lines))
for i in lines:
    if i.startswith("Coding"):
       print("skip", '->', i.strip())
    else:
       print("keep", '->', i.strip())
file.close()