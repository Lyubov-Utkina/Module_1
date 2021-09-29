
Lyubov Utkina     https://www.kaggle.com/lemura


Задача
Прогнозирование стоимости автомобиля по характеристикам.
https://www.kaggle.com/c/sf-dst-car-price-prediction-part2/overview


Часть проекта, включающая в себя обработку данных, основана на предыдущем проекте,
который был выполнен в команде 'BALU'
https://github.com/Lyubov-Utkina/Modules/blob/master/module_6/car-price-balu.ipynb
В каггле: https://www.kaggle.com/alexeyblinnikov/car-price-balu


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
https://github.com/Lyubov-Utkina/Modules/blob/master/module_7/Project_7.ipynb





