# Итоговое задание №7

### [Назад в Содержание ⤶](/README.md)

## Задача
Дан фрагмент кода, который выполняет операции над списком строк. Код написан в _императивном_ стиле, использует 
изменяемые переменные и циклы. Необходимо преобразовать этот код в _функциональный_ стиль. В качестве решения пришлите 
ссылку на свой гитхаб репозиторий. Обязательно должны быть комментарии, что и где Вы поменяли.  

### Входные данные

```scala
object StringProcessor {
  def processStrings(strings: List[String]): List[String] = {
    var result = List[String]()
    for (str <- strings) {
      if (str.length > 3) {
        result = result :+ str.toUpperCase
      }
    }
    result
  }

  def main(args: Array[String]): Unit = {
    val strings = List("apple", "cat", "banana", "dog", "elephant")
    val processedStrings = processStrings(strings)
    println(s"Processed strings: $processedStrings")
  }
}
```

## Решение задачи
1. Для начала избавимся от возвращаемой переменной `result`, будем возвращать результат непосредственно из цепочки методов.
2. Используем методы высшего порядка:
    - map для преобразования строк в верхний регистр,
    - filter для отбора строк длиной больше 3 символов.

```scala
object StringProcessor {
  // Преобразуем метод processStrings в функциональный стиль
  def processStrings(strings: List[String]): List[String] = {
    // Используем метод filter для отбора строк длиной больше 3 символов
    // Затем применяем метод map для преобразования строк в верхний регистр
    strings.filter(_.length > 3).map(_.toUpperCase)
  }

  def main(args: Array[String]): Unit = {
    val strings = List("apple", "cat", "banana", "dog", "elephant")
    val processedStrings = processStrings(strings)
    println(s"Processed strings: $processedStrings")
  }
}
```

Код стал короче и более читаемым благодаря использованию функциональных методов.

<img src="/img/task_7.png" width="40%">

Работает в соответствии с нашими ожиданиями.

[Итоговое задание №7 (код)](task_7/StringProcessor.scala)