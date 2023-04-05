def say_hello(turno):
    turno = turno.upper()

    if turno == 'M':
        return 'Bom dia!'
    elif turno == 'V':
        return 'Boa tarde!'
    elif turno == 'N':
        return 'Boa noite!'
    else:
        return None


if __name__ == '__main__':
    print('Em qual turno você estuda (M/V/N)?')
    print('''
    M - matutino
    V - Vespertino
    N - Noturno
    ''')
    turno = str(input())
    cumprimentos = say_hello(turno)
    print(cumprimentos)