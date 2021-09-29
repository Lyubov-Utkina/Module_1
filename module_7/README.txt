
Lyubov Utkina     https://www.kaggle.com/lemura


Задача
Прогнозирование стоимости автомобиля по характеристикам.
https://www.kaggle.com/c/sf-dst-car-price-prediction-part2/overview


Результаты.

1. На тренировочной выборке лучше всего сработал блэндинг CatBoost и нейросети, 
   на вход которой подаются табличные данные и текст. MAPE = 10.76%.
2. На тестовой выборке также лучшие результаты показал блэндинг. На тестовой выборке MAPE = 11.35%
3. Из моделей лучшие результаты получены для CatBoost: MAPE = 11.85%
4. Нейросеть (табличные данные + текст) показала результат хуже, чем просто CatBoost


Входные данные

test.csv - Тестовая выборка данных для предсказаний на Kaggle
https://www.kaggle.com/c/sf-dst-car-price-prediction-part2/data?select=test.csv

train.csv - Обучающая выборка
https://www.kaggle.com/c/sf-dst-car-price-prediction-part2/data?select=train.csv

sample_submission.csv - Файл содержит формат ответа
https://www.kaggle.com/c/sf-dst-car-price-prediction-part2/data?select=sample_submission.csv

img - папка с изображениями авто из объявлений
https://www.kaggle.com/c/sf-dst-car-price-prediction-part2/data?select=img


Ноутбуки

Project_7.ipynb - Основной Notebook, в котором производилась работа.





