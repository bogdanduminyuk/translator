# Приложение для работы с онлайн словарями
Это приложение используется для поиска:
- перевода
- определений
- синонимов
- антонимов

## Словари
Для получения нужной информации используются следующие *online* словари:
- [Oxford Dictionaries](https://en.oxforddictionaries.com/)
- [WooordHunt](https://wooordhunt.ru/)

Словарь *Oxford Dictionary* предоставляет API (*Application Programming Interfaces*) для работы со словарем из внешних приложений. Использование API накладывает следующие **ограничения**:
| Тип ограничения | Значение |
| ------ | ------ |
| Количество запросов в месяц| 3000 |
| Количество запросов в минуту | 60 |

## Входящие данные
В качестве входящих данных программе передается файл со списком слов на английском языке, а также что именно для них нужно получить: перевод, определения, синонимы или антонимы (или все сразу).

## Исходящие данные
В результате работы приложения получается файл с таблицей вида:
| № п/п | Слово (англ.) | Перевод | Синонимы | Антонимы | Определение
| :------: | ------ | ------ | ------ | ------ | ------ |
| 1 | white | белый, седой, бледный, серебристый, чистый, белый, белила, белизна, белый цвет, белок | colourless, unpigmented, undyed, bleached, natural; pale, clear, transparent | black | Of the colour of milk or fresh snow, due to the reflection of all visible rays of light; the opposite of black; belonging to or denoting a human group having light-coloured skin (chiefly used of peoples of European extraction)
| 2 | brain | мозг, мозги, головной мозг, ум, голова, размозжить голову | cerebrum, cerebral matter; intelligence, intellect, intellectual capacity, mental capacity, brainpower, cleverness, wit, wits, powers of reasoning, reasoning, wisdom, sagacity, acumen, discernment, shrewdness, judgement, understanding, common sense, sense; mind, head | dunce, idiot | An organ of soft nervous tissue contained in the skull of vertebrates, functioning as the coordinating centre of sensation and intellectual and nervous activity; intellectual capacity
