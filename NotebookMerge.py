import os

print('=== Science Notes ===')
with open('science_notes.txt', 'r') as f:
     for line in f:
         print(line.strip())
print()