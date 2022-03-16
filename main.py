import random




def play():
    def kolvo_skota():
        print('введите чиcло от 1 до 10')
        n = int(input())
        if n > 10 or n < 1:
            print('попробуй еще разок')
            return kolvo_skota()
        else:
            return n

    a = kolvo_skota()
    ls = []
    while len(ls) != a:
        b = random.randint(1, 9)
        if str(b) not in ls:
            ls.append(str(b))
    #print(ls)                        для отладки

    while True:
        print('введите', a, 'разных цифр в одну строку через пробел')
        n = input().split()
        #print(n)                     тоже
        if n == ls:
            break
        else:
            counter1 = 0
            counter2 = 0
            for i in range(len(ls)):
                if ls[i] == n[i]:
                    counter1 += 1
                if n[i] in ls:
                    counter2 += 1
            print('cows =', counter1, 'bools =', counter2)

play()