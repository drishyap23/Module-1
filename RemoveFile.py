import os

if os.path.exists('all_notes.txt'):
    os.remove('all_notes.txt')
    print('all_notes.txt deleted.')
else:
    print('all_notes.txt does not exist.')