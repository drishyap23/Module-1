word = input('Skip lines starting with: ')

file = open('bucket_list.txt', 'r')
for line in file:
    if line.startswith(word):
        print('skip ->', line.strip())
    else:
        print('keep ->', line.strip())
file.close()