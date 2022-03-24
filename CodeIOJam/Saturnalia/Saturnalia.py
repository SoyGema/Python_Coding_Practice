import sys
data = sys.stdin

def box_corners(line):
    print('+' + ' ' + '-'*len(line) + ' ' + '+')

def build_message(line):
    print( str('| ') + line + str(' |'))

for i in range(1,len(data)):
    print('Case' + ' #' + str(i) + ':')
    box_corners(data[i])
    build_message(data[i])
    box_corners(data[i])
