

import pandas as pd

# Загрузка данных
df = pd.read_excel('AmazonBooks.xlsx')

# Задание №2: Сортировка по году возрастания
df_sorted = df.sort_values(by='Year', ascending=True)

# Задание №3: Срез книг дороже 20$
df_expensive = df[df['Price'] > 20]

# Задание №4: Выбор столбцов
df_subset = df[['Name', 'User Rating', 'Reviews']]

# Задание №5: Уникальные авторы за 2011 год с отзывами > 75-го квантиля
# Фильтрация за 2011 год
df_2011 = df[df['Year'] == 2011]

# Расчёт 75-го квантиля
q75 = df_2011['Reviews'].quantile(0.75)
print(q75)

# Фильтрация авторов с хотя бы одной книгой > q75
authors_above_q75 = df_2011[df_2011['Reviews'] > q75]['Author'].unique().tolist()
print(authors_above_q75)

# Задание №6: Создание категорий и кодов
df['genre_categories'] = df['Genre'].astype('category')
df['genre_codes'] = df['Genre'].astype('category').cat.codes