import csv
import datetime

def is_last_month(date_str):
    dt = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    now = datetime.datetime.now()
    last_month = datetime.datetime(now.year, now.month-1, now.day)
    return dt >= last_month

def read_file(filename, product_name):
    try:
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == product_name and is_last_month(row[1]):
                    print('Товар "{}" изменил цену на {} рублей {}'.format(row[0], row[2], row[1]))
    except FileNotFoundError:
        print('Ошибка: файл не найден.')
    except:
        print('Произошла ошибка при чтении файла.')

filename = 'products.txt' # пример имени файла
product_name = 'Product 1' # замените на нужное название товара
read_file(filename, product_name)
