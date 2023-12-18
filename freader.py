from os import strerror

try:
    counter = 0
    stream = open('try.text', 'rt')
    char = stream.read(1)
    while char !='':
        print(char, end='')
        counter += 1
        char = stream.read(1)
        stream.close
        print("\n\n Characters in file:", counter)
except IOError as e:
    print("I/O error occured:", strerror(e.errno) )
    
