import psycopg2
import csv

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='121'
)

cur = conn.cursor()

# Заполнение таблиц данными из файлов
paths = ['C:/Users/MARAT/PycharmProjects/postgres-homeworks/homework-1/north_data/customers_data.csv',
         "C:/Users/MARAT/PycharmProjects/postgres-homeworks/homework-1/north_data/employees_data.csv",
         "C:/Users/MARAT/PycharmProjects/postgres-homeworks/homework-1/north_data/orders_data.csv"]

for path in paths:
    with open(path, 'r') as file:
        next(file)  # Пропускаем заголовок
        table_name = path.split('/')[-1].split('.')[0]  # Получаем имя таблицы из имени файла
        cur.copy_from(file, table_name, sep=';')

# Фиксация изменений и закрытие соединения
conn.commit()
conn.close()