import pandas as pd
import random

# Генерация данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Печать первых 5 строк для проверки
print("Исходные данные:")
print(data.head)

# Преобразование в One Hot Encoding
unique_values = data['whoAmI'].unique()

for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

# Удаление исходного столбца
data = data.drop('whoAmI', axis=1)

# Печать первых 5 строк для проверки результата
print("\nOne Hot Encoding данные:")
data.head()