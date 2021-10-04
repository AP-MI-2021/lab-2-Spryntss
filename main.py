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
    Transforma numarul din baza 10 in forma binara (baza 2)
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

def is_palindrome(n):
    '''
    Verifica daca un numar este palindrom sau nu
    :param n: numar intreg
    :return: returneaza adevarat sau fals
    '''
    n = int(n)
    copie = n
    rez = 0
    while n:
        cifra=n%10
        rez=rez*10+cifra
        n=n//10
    if(copie==n):
        return True
    else:
        return False

def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(100) == False
    assert is_palindrome(10501) == True

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
test_is_palindrome()

option = '''
Daca doriti sa aflati cel mai mare numar prim, mai mic decat o valoare, scrieti "1".  
Daca doriti sa transformati un numar din baza 10 in baza 2, scrieti "2".
Daca doriti sa verificati daca un numar este sau nu palindrom, scrieti "3". 
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
        elif optiune == '3':
            numar = input("Scrieti numarul pe care doriti sa-l verificati: ")
            print(f"Numarul dat este palindrom?" + str(is_palindrome(numar)))
        elif optiune == 'x':
            break
        else: print("Comanda neexistenta")

menu()