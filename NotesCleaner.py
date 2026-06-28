f = open('class_notes.txt', 'r')
n = int(input("Enter how many characters to preview: "))
print(f.read(20))
f.close()