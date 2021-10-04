from math import *

def get_largest_prime_below(n):
    '''
    Returneaza cel mai mare numar prim, mai mic decat parametrul n
    :param n: numar intreg
    :return: Returneaza numarul prim
    '''
    for i in range(n-1, 1, -1):
        ok=1
        for j in range(2, int(sqrt(i))+1):
            if i%j==0:
                ok=0
        if ok == 1:
            return i

def get_base_2(n:str):
    '''
    :param n: numarul in baza 10, sub forma de string
    :return: returneaza sub forma de string, numarul convertit in baza 2
    '''
    n = int(n)
    lst = []
    s = ''
    while n:
        lst.append(n%2)
        n = n // 2
    for i in range(len(lst)-1, -1, -1):
        s = s + str(lst[i])
    return s

def test_get_largest_prime_below():
    assert get_largest_prime_below(20) == 19
    assert get_largest_prime_below(2) == None
    assert get_largest_prime_below(16) == 13

def test_get_base_2():
    assert get_base_2(10) == '1010'
    assert get_base_2(123) == '1111011'
    assert get_base_2(16) == '10000'

test_get_largest_prime_below()
test_get_base_2()

option = '''
Daca doriti sa aflati cel mai mare numar prim, mai mic decat o valoare, scrieti "1".  
Daca doriti sa transformati un numar din baza 10 in baza 2, scrieti "2". 
Daca doriti sa opriti programul, scrieti x 
'''

def menu():
    while True:
        optiune = input(option)
        if optiune == '1':
            numar = int(input("Scrieti valoarea:"))
            print(f"Cel mai mare numar prim, mai mic decat {numar}, este: " + str(get_largest_prime_below(numar)))
        elif optiune == '2':
            numar = input("Scrieti numarul pe care doriti sa-l convertiti: ")
            print(f"Numarul {numar} convertit in baza 2 este: " + get_base_2(numar))
        elif optiune == 'x':
            break
        else: print("Comanda neexistenta")

menu()