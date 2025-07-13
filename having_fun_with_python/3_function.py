def find_chracter(s, c):
    '''
    it searchs for c is s string,
    returns True or False.
    '''
    for chracter in s:
        res = False
        if c == chracter:
            res = True
            break
    return res

def get_string():
    '''
    gets string from user.
    '''
    input('give me your string: ')

def get_chracter():
    '''
    gets chracter from user.
    '''
    input('give me your chracter: ')

print("Hello and welcome!")

my_string = input('give me your string: ')
my_chracter = input('give me your chracter: ')
final_result = find_chracter(my_string, my_chracter)

print(f"is there any {my_chracter} in the string: {final_result} ")





