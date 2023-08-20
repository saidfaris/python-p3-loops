#!/usr/bin/env python3
def happy_new_year():
    # code goes here!
    pass
    i = 10

    while i != 0:
        print(f'{i}')
        if i == 1:
            print('Happy New Year!')
        i -= 1


def square_integers(int_list):
    # code goes here!
    pass
    new_int = list()
    for number in int_list:
        numbers = number * number
        new_int.append(numbers)

    return new_int    

def fizzbuzz():
    # code goes here!
    pass
    i = 0
    while i < 100:
        i+=1
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')    
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:    
            print(f'{i}')


happy_new_year()
arr = square_integers([2,3,4,5,6,7])
print(arr)
fizzbuzz()