def show_menu():
    print('1. Minimul a trei numere.')
    print('2. Determinarea daca un numar dat este prim. ')
    print('3. Afisare primalitate pentru elementele uneui liste. ')
    print('4. Determinarea inversului unui numar dat. ')
    print('x. Iesire.')


def read_list():
    lst_str = input('Dati numerele separate prin spatiu: ')
    lst_str_split = lst_str.split(' ')
    lst_int = []
    for lst in lst_str_split:
        lst_int.append(int(lst))
    return lst_int


def get_minim(a: int, b: int, c: int) -> int:
    '''
    Determina minimul dintre 3 numere date.
    :param a: Primul numar.
    :param b: Al doilea numar.
    :param c: Al treilea numar.
    :return: Minimul dintre a,b,c.
    '''
    minim = a
    if b < minim:
        minim = b
    if c < minim:
        minim = c
    return minim


def test_get_minim():
    assert get_minim(3, 4, 5) == 3
    assert get_minim(15, 25, 1) == 1
    assert get_minim(4, 4, 4) == 4
    assert get_minim(12, 7, 56) == 7


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    else:
        for i in range(2, n-1):
            if n % i == 0:
                return False
        return True

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(1) == False
    assert is_prime(8) == False
    assert is_prime(17) == True
    assert is_prime(600456) == False

def get_reverse(n: int) -> int:
    invers = 0
    while n:
        invers = invers * 10 + n % 10
        n //= 10
    return invers

def test_get_reverse():
    assert get_reverse(3) == 3
    assert get_reverse(12) == 21
    assert get_reverse(467) == 764
    assert get_reverse(9786) == 6879

def main():
    while True:
        show_menu()
        optiune = input('Alegeti o optiune: ')
        if optiune == '1':
            n1 = int(input('Primul numar: '))
            n2 = int(input('Al doilea numar: '))
            n3 = int(input('Al treilea numar: '))
            print(f'Minimul dintre {n1}, {n2}, {n3} este {get_minim(n1, n2, n3)}')
        elif optiune == '2':
            n = int(input('Alegeti un numar: '))
            if is_prime(n):
                print(f'Numarul {n} este prim!')
            else:
                print(f'Numarul {n} nu este prim!')
        elif optiune == '3':
            lista = read_list()
            for i in range(len(lista)):
                if is_prime(lista[i]):
                    print(f'Elementul {lista[i]} este prim!')
                    print()
                else:
                    print(f'Elementul {lista[i]} nu este prim!')
                    print()
        elif optiune == '4':
            n = int(input('Alegeti un numar: '))
            print(f'Inversul lui {n} este {get_reverse(n)}.')
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida! Incercati din nou!')


if __name__ == '__main__':
    test_get_minim()
    test_is_prime()
    test_get_reverse()
    main()
