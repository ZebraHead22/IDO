import pandas as pd
import requests
import sqlalchemy as sql

# 1. Загрузите данные из файла .ods (лист 'Sheet1')
# Для работы с .ods-файлами требуется установить пакет 'odfpy': pip install odfpy
df = pd.read_excel('Employee_Salary_Dataset.ods', engine='odf', sheet_name='Sheet1')

# 2. Выведите общую информацию о датафрейме
print("Информация о датафрейме:")
print(df.info())

# 3. Приведите все названия столбцов к нижнему регистру
df.columns = df.columns.str.lower()

print(df.head())
print(df.shape)

# 4. Удалите выбросы по зарплате (salary) по методу IQR3 (тройной межквартильный интервал)
q1 = df['salary'].quantile(0.25)
q3 = df['salary'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 3 * iqr
upper_bound = q3 + 3 * iqr
df_without_outliers = df[(df['salary'] >= lower_bound) & (df['salary'] <= upper_bound)]
print("\nРазмер датафрейма без выбросов по зарплате:", df_without_outliers.shape)
print(df_without_outliers.head(20))

# # 5. Получите таблицу со среднемесячными доходами в субъектах Сибирского ФО из Википедии
# wiki_url = 'https://ru.wikipedia.org/wiki/Доходы_населения_России'

# try:
#     # Используем requests для получения страницы и явно указываем кодировку
#     response = requests.get(wiki_url)
#     response.encoding = 'utf-8'  # Указываем кодировку
#     html_content = response.text

#     # Извлекаем таблицы из HTML-кода
#     tables = pd.read_html(html_content, decimal=',')
    
#     df_incomes = None
#     for table in tables:
#         # Если в таблице есть хотя бы одно упоминание "Сибирский" — предполагаем, что это нужная таблица
#         if table.astype(str).apply(lambda x: x.str.contains("Сибирский", case=False, na=False)).any().any():
#             df_incomes = table.copy()
#             break

#     if df_incomes is not None:
#         print("\nНайденная таблица со среднемесячными доходами (первые строки):")
#         print(df_incomes.head())
#     else:
#         print("Таблица с данными о доходах для Сибирского ФО не найдена.")
# except Exception as e:
#     print("Ошибка при извлечении таблиц со страницы:", e)

df = pd.read_html(
    'https://ru.wikipedia.org/wiki/%D0%94%D0%BE%D1%85%D0%BE%D0%B4%D1%8B_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8#%D0%9C%D0%B5%D0%B4%D0%B8%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F_%D0%B7%D0%B0%D1%80%D0%BF%D0%BB%D0%B0%D1%82%D0%B0',
    match='Сибирский ФО',
    attrs={'class': 'wikitable'}
)[0]
print(df)

# 6. Запишите загруженный датафрейм с доходами в базу данных SQLite, используя SQLAlchemy
if df is not None:
    engine = sql.create_engine('sqlite:///incomes.db')
    df.to_sql("incomes", engine, if_exists="replace", index=False)
    print("\nДанные о доходах успешно записаны в базу данных SQLite (таблица 'incomes').")
