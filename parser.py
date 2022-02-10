import sys


print('arg 1, 2 and 3 are {},{},{}'.format((str(sys.argv[1])),(str(sys.argv[2])),str(sys.argv[3])))

with open('textfile.txt', 'r+') as f:
    content = f.read()
    f.seek(0,0)
    f.write((str(sys.argv[1])).rstrip('\r\n') + '\n' + content)


with open('textfile.txt', 'a') as f:
    f.write(str(sys.argv[2])+ '\n' + str(sys.argv[3])+ '\n' )


        
