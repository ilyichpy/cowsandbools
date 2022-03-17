import random


def play():
    def adding_animals():
        print('введите чиcло от 1 до 10')
        while True:
            n = int(input())
            if n > 10 or n < 1:
                print('неверное значение')
            else:
                return n
                break


    a = adding_animals()
    lst = []
    while len(lst) != a:
        b = random.randint(1, 9)
        if str(b) not in lst:
            lst.append(str(b))
    #print(lst)

    while True:
        print('введите', a, 'разных цифр в одну строку без пробела')  #no more space between your_input
        your_input = int(input())
        your_input = [str(num) for num in str(your_input)]
        #print(your_input)
        if your_input == lst:
            print('вы выиграли!')
            break
        else:
            counter1 = 0
            counter2 = 0
            for i in range(len(lst)):
                if lst[i] == your_input[i]:
                    counter1 += 1
                if your_input[i] in lst and your_input[i] != lst[i]:
                    counter2 += 1
            print('cows =', counter1, 'bools =', counter2)

play()
