import random


def play():
    def adding_animals():
        print('введите чиcло от 1 до 10')
        while True:
            n = int(input())
            if n > 10 or n < 1:
                print('неверное значение')
            else:
                return n == int(input())


    a = adding_animals()
    lst = []
    while len(lst) != a:
        b = random.randint(1, 9)
        if str(b) not in lst:
            lst.append(str(b))
    #print(ls)                        для отладки

    while True:
        print('введите', a, 'разных цифр в одну строку через пробел')
        n = input().split()
        #print(n)                     тоже
        if n == lst:
            break
        else:
            counter1 = 0
            counter2 = 0
            for i in range(len(lst)):
                if lst[i] == n[i]:
                    counter1 += 1
                if n[i] in lst:
                    counter2 += 1
            print('cows =', counter1, 'bools =', counter2)

play()