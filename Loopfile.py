file = open('bucket_list.txt', 'r')

for line in file:
    print(line.strip())

file.close()