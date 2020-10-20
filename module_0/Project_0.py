#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Угадай число в диапазоне 1-100

import numpy as np
number = np.random.randint(1,101)    # загадали число
print ("Загадано число от 1 до 100")

def game_core_v3(number):
    """Функция делит диапазон пополам и работает с той частью, в которой находится загаданное число.
    Функция принимает загаданное число и возвращает число попыток
    """
    count = 1    # счетчик попыток
    begin = 1
    end = 101
    predict = (begin+end) // 2    # Нашли середину диапазона
    
    while number != predict:
        count += 1
        if number > predict: 
            begin = predict + 1    # Отсекли неподходящую часть диапазона
            predict = (begin+end) // 2
        elif number < predict: 
            end = predict - 1    # Отсекли неподходящую часть диапазона
            predict = (begin+end) // 2
            
    return(count) # выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# Проверяем
score_game(game_core_v3)


# In[ ]:




