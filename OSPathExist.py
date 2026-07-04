import os

if os.path.exists('class_notes.txt'):
    print('class_notes.txt already exists - overwriting')
else:
    print('class_notes.txt not found - creating now')