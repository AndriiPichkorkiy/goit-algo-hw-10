import pulp

model = pulp.LpProblem("Total product", pulp.LpMaximize)  # Максимізація

# Кількість продукту А
A = pulp.LpVariable('Лимонад', lowBound=0, cat='Integer')

B = pulp.LpVariable('Фруктовий сік', lowBound=0,
                    cat='Integer')  # Кількість продукту Б

# Функція цілі (Максимізація прибутку)
model += A + B, "Total product"

# Додавання обмежень
model += 2 * A + 1 * B <= 100  # Обмеження для Води
model += 1 * A <= 50  # Обмеження для Цукру
model += 1 * A <= 30  # Обмеження для Лимонного соку
model += 2 * B <= 40  # Обмеження для Фруктового пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print(F"Виробляти продуктів {A.name}:", A.varValue)
print(F"Виробляти продуктів {B.name}:", B.varValue)
print(
    f"Максимальна кількість вироблених продуктів: {pulp.value(model.objective)}")
