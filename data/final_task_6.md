# Итоговое задание №6

### [Назад в Содержание ⤶](/README.md)

## Задача
Задание состоит из двух частей. Необходимо сгенерировать тестовые данные и провести их анализ с помощью **PySpark**. 
В качестве ответа приложите только код на **Spark**. Формат решения `.ipynb`.  

## Часть 1. Генерация информации
### Суть задачи
Используем библиотеку **Faker** для генерации логов веб-сервера.  

### Выходные данные
Логи содержат следующую информацию:
- _IP-адрес клиента_  
- _Временная метка запроса_  
- _HTTP-метод (GET, POST, etc.)_  
- _URL запроса_  
- _Код ответа (200, 404, etc.)_  
- _Размер ответа в байтах_  

### Формат выходных данных
После генерации 100,000 записей логов сохраняем их в _CSV_-файл `web_server_logs.csv`. 

Перед генерацией не забудьте выполнить в терминале команду: 

```bash
pip install faker
```

### Код для генерации
[Генерация тестовых данных (код)](task_6/final_task_6.1.py)

### Пример получившихся данных

<img src="/img/task_6.1.png" width="70%">

## Часть 2. Анализ информации
### Подзадачи
1. Сгруппировать данные по _IP_ и посчитать количество запросов для каждого IP, вывести 10 самых активных IP.  
2. Сгруппировать данные по _HTTP_-методу и посчитать количество запросов для каждого метода.  
3. Профильтровать и посчитать количество запросов с кодом ответа 404.  
4. Сгруппировать данные по дате и просуммировать размер ответов, отсортировать по дате.  

### Формат вывода

<img src="/img/task_6.2.png" width="30%">

## Решение задачи
#### 1. Подгружаем необходимые модули и создаем сессию Spark

```python
spark = SparkSession.builder \
    .appName("Log Analysis") \
    .getOrCreate()
```

#### 2. Загружаем данные логов в DataFrame

```python
logs_df = spark.read.csv("web_server_logs.csv", header=True, inferSchema=True)
```

#### 3. Группируем данные по IP и считаем количество запросов для каждого IP

```python
active_ips = logs_df.groupBy("ip").agg(count("*").alias("request_count")) \
    .orderBy(col("request_count").desc()) \
    .limit(10)

print("Top 10 active IP addresses:")
active_ips.show()
```

#### 4. Группируем данные по HTTP-методу и считаем количество запросов для каждого метода

```python
http_methods = logs_df.groupBy("method").agg(count("*").alias("request_count"))

print("Request count by HTTP method:")
http_methods.show()
```

#### 5. Фильтруем и считаем количество запросов с кодом ответа 404

```python
not_found_count = logs_df.filter(col("response_code") == 404).count()

print(f"Number of 404 response codes: {not_found_count}")
```

#### 6. Группируем данные по дате и суммируем размер ответов, сортируя по дате

```python
response_size_by_date = logs_df.groupBy(to_date(col("timestamp")).alias("date")) \
    .agg(sum("response_size").alias("total_response_size")) \
    .orderBy("date")

print("Total response size by day:")
response_size_by_date.show()
```

#### 7. Останавливаем сессию Spark

```python
spark.stop()
```

[Итоговое задание №6 (код)](task_6/final_task_6.2.py)