import sys


data = ['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
for line in sys.stdin.read().splitlines()[1::]:
    print(''.join([str(data.index(row)) for row in line.split()]))
