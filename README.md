
markdown
## Описание
<font color="lightpink">

Цель проекта - изучение функциональности и возможностей различных библиотек, таких как Pandas, psycopg2 (Postgress), SQLite,DuckDB и других, а также их применение в различных сферах.

## Как пользоваться

1. **Клонирование репозитория**
   ```sh
   git clone https://github.com/Borshick02/laba_bd3.git
   ```

2. **Предустановка **
    ```sh
    pip install duckdb
    ```
   -пожалуйста,не забудьте скачать необходимые библиотеки,по примеру выше.

3. **Подготовка данных**
   - скачайте и откройте файлы nyc_yellow_tiny.csv и nyc_yellow_big.csv в корневую директорию проекта.Или используйте свои тестовые данные.
ссылка на файлы
 ```sh
https://drive.google.com/file/d/1BlGqraARshWU1FRSZtjTcISfRP3e8Usx/view?usp=drive_link
https://drive.google.com/file/d/1XWCk4XmgdNUZ8E42ktjGpeeKZeTO9YnJ/view?usp=drive_link
 ```

4. **Конфиг файл и запуск тестирования**
   - Откройте файл benchmarkconfig.json и внесите необходимые изменения в запросы в соответствии с вашими потребностями.В данном файле вы можете изменять запросы для вашей таблицы,запросы по которым будет измеряться время.
   - Здесь вы также можете изменить название файла,на котором будут проводиться замеры.Укажите файл nyc_yellow_tiny.csv или свой файл в качестве тестовых данных.
   
