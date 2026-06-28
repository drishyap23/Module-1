file = open('bucket_list.txt', 'r')
lines = file.readlines()
file.close()

out = open('odd_lines.txt', 'w')

for i in range(0, len(lines), 2):
    out.write(lines[i])

out.close()
print('Odd lines saved to odd_lines.txt')