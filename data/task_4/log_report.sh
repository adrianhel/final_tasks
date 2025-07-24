#!/bin/bash
# Установка кодировки
export LANG=en_US.UTF-8

# Файл с логами
LOG_FILE="access.log"

# Подсчет общего количества запросов
total_requests=$(awk 'NF' "$LOG_FILE" | wc -l)

# Подсчет уникальных IP-адресов
unique_ips=$(awk '{print $1}' "$LOG_FILE" | sort -u | wc -l)

# Подсчет количества запросов по методам
method_counts=$(awk '{print $6}' "$LOG_FILE" | sort | uniq -c)

# Найти самый популярный URL
popular_url=$(awk '{print $7}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -n 1)

# Создание отчета
{
  echo "Отчет о логе вебсервера"
  echo "======================="
  echo "Общее количество запросов: $total_requests"
  echo "Количество уникальных IP-адресов: $unique_ips"
  echo ""
  echo "Количество запросов по методам:"
  echo "$method_counts"
  echo ""
  echo "Самый популярный URL: $popular_url"
} > report.txt

echo "Отчет создан в report.txt"
