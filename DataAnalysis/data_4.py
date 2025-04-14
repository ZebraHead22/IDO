import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Загрузите датасет в виде датафрейма
df = pd.read_csv('Customer-Churn-Records.csv')

# 2. Приведите все названия столбцов к нижнему регистру и замените пробелы на знак '_'
df.columns = df.columns.str.lower().str.replace(' ', '_')
print(df.columns)
# 3. Выведите информацию по этому датафрейму
print("Информация о датафрейме:")
print(df.info())
print("\nПервые 5 строк датафрейма:")
print(df.head())

# 4. Отобразите в виде столбчатой диаграммы страны ('geography') по среднему балансу счетов клиентов банка ('balance').
# Группируем по странам и вычисляем средний баланс
avg_balance_by_geography = df.groupby('geography')['balance'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=avg_balance_by_geography, x='geography', y='balance', palette='viridis')
plt.title('Средний баланс по странам')
plt.xlabel('Страна')
plt.ylabel('Средний баланс')
plt.show()

# 5. Добавьте к существующему датафрейму столбец, содержащий средний баланс счета клиента по стране.
# Один из вариантов – использование map с заранее вычисленным словарем средних значений:
avg_balance_dict = df.groupby('geography')['balance'].mean().to_dict()
df['avg_balance_by_country'] = df['geography'].map(avg_balance_dict)

print("\nДатафрейм с добавленным столбцом среднего баланса по стране:")
print(df.head())

# 6. Отобразите столбчатую диаграмму с накоплением для общего количества продуктов по различным странам и полу клиентов банка.
# Предполагаем, что в наборе данных есть столбец 'num_of_products', обозначающий количество продуктов.
# Группируем данные по 'geography' и 'gender', суммируем количество продуктов, затем строим накопительную диаграмму.
df_products = df.groupby(['geography', 'gender'])['numofproducts'].sum().unstack()

df_products.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Paired')
plt.title('Общее количество продуктов по странам и полу')
plt.xlabel('Страна')
plt.ylabel('Общее количество продуктов')
plt.legend(title='Пол')
plt.tight_layout()
plt.show()
