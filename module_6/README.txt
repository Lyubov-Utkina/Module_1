Проект выполнен в команде 'BALU':

Lyubov Utkina     https://www.kaggle.com/lemura

Alexey Blinnikov  https://www.kaggle.com/alexeyblinnikov


Задача
Прогнозирование стоимости автомобиля по характеристикам.
https://www.kaggle.com/c/sf-dst-car-price-prediction/overview

Результаты.

В результате работы удалось существенно улучшить baseline.
Лучшие результаты на обучающих данных показала модель CatBoost, значение метрики MAPE 0.1325
В соревновании на каггл лучшие результаты у RandomForest - 12.24%.

Хотя в процессе командной работы сложилось некоторое разделение труда, работали параллельно, 
вникая в детали и обмениваясь опытом и идеями.



Входные данные

test.csv - Тестовая выборка данных для предсказаний на Kaggle
https://www.kaggle.com/c/sf-dst-car-price-prediction/data?select=test.csv

all_auto_ru_09_09_2020.csv - Старый парсинг данных, предоставленный с baseline проекта.
https://www.kaggle.com/sokolovaleks/parsing-all-moscow-auto-ru-09-09-2020?select=all_auto_ru_09_09_2020.csv

extended_train.csv - Результат нашего парсинга
https://www.kaggle.com/alexeyblinnikov/car-price-spring-2021?select=extended_train.csv

sample_submission.csv - Файл содержит формат ответа
https://www.kaggle.com/c/sf-dst-car-price-prediction/data?select=sample_submission.csv


Ноутбуки
car_Price_balu.ipynb - Основной Notebook, в котором производилась работа.
https://github.com/Lyubov-Utkina/Modules/blob/master/module_6/car-price-balu.ipynb
В каггле: https://www.kaggle.com/alexeyblinnikov/car-price-balu

CarPrice_parsing_april_2021.ipynb - Ноутбук с парсингом данных.
https://github.com/Lyubov-Utkina/Modules/blob/master/module_6/CarPrice_parsing_april_2021.ipynb

Model_testing.ipynb - Ноутбук с поиском моделей по Lazy Predict и подбору оптимальных гиперпараметров.
https://github.com/Lyubov-Utkina/Modules/blob/master/module_6/Model_testing.ipynb


Данные
alt_data.csv - обработанные данные, использовали для тестирования моделей
https://github.com/Lyubov-Utkina/Modules/blob/master/module_6/alt_data.csv

band_model.csv - пары бренд-модель для парсинга.
https://github.com/Lyubov-Utkina/Modules/blob/master/module_6/band_model.csv

Данные, полученные в результате парсинга, а также тестовую выборку на github не загрузила из-за размера.

