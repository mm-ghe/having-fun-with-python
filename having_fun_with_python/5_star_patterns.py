def stars1(row):
    for i in range(1, row + 1):
        print(i * '*')
        
def stars2(row):
    for i in range(1, row + 1):
        print((row - i) * ' ', i * '*')

def stars3(row):
    for i in range(1, row + 1):
        print((row - i) * ' ', (i*2 - 1) * '*')
