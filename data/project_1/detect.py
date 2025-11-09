import chardet

file_path = "C:/Users/andy/PycharmProjects/final_tasks/data/project_1/notebooks/russian_houses.csv"

# Читаем только первые 10КБ для скорости
with open(file_path, 'rb') as file:
    raw_data = file.read(10000)
    encoding = chardet.detect(raw_data)['encoding']

print(f"Кодировка: {encoding}")
