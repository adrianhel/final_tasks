
















## Решение

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
    // Вызов метода processStrings и получение обработанных строк
    val processedStrings = processStrings(strings)
    println(s"Processed strings: $processedStrings")
  }
}
```