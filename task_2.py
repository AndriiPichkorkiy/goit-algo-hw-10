import scipy.integrate as spi
import matplotlib.pyplot as plt
import numpy as np
import random


# Визначення функції та межі інтегрування


def f(x):
    return x ** 2


a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()
fig.patch.set_facecolor('#2e2e2e')  # Темний фон для фігури
ax.set_facecolor('#1e1e1e')  # Темний фон для графіка

# Малювання функції
ax.plot(x, y, color='#FFA07A', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='#4B4B4B', alpha=0.3)

# Метод Монте-Картло


def is_in_range(x, y):
    return y <= f(x)


# Генерація випадкових точок

def monte_carlo(num_samples=10000):
    # 1. Визначення моделі або системи.
    inside_figure = 0
    x_inside, y_inside = [], []
    x_outside, y_outside = [], []
    # 2. Генерація випадкових вхідних даних
    for _ in range(num_samples):
        pointer_x = random.uniform(a, b)
        pointer_y = random.uniform(0, max(iy))
        # 3. Виконання обчислень
        if is_in_range(pointer_x, pointer_y):
            inside_figure += 1
            x_inside.append(pointer_x)
            y_inside.append(pointer_y)
        else:
            x_outside.append(pointer_x)
            y_outside.append(pointer_y)

    # 4. Агрегування та аналіз результатів
    area_rect = (b - a) * max(iy)

    area_estimate = area_rect * (inside_figure / num_samples)
    return area_estimate, x_inside, y_inside, x_outside, y_outside


# Задаємо кількість випадкових точок
num_samples = 10_000

# Запускаємо метод Монте-Карло для обчислення інтеграла
area_estimate, x_inside, y_inside, x_outside, y_outside = monte_carlo(
    num_samples)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x', color='white')
ax.set_ylabel('f(x)', color='white')

# Візуалізація результатів
plt.scatter(x_inside, y_inside, color='#00CED1',
            s=1, label='Точки всередині кола')
plt.scatter(x_outside, y_outside, color="orange",
            s=1, label='Точки поза колом')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' +
             str(a) + ' до ' + str(b), color='white')
plt.legend(facecolor='#2e2e2e', edgecolor='white')
plt.grid(color='#4B4B4B')
plt.show()


# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Результат:")
print(
    f"Оцінка площі методом Монте-Карло з {num_samples} випадкових точок: {area_estimate}")
print(f"Аналітичний результат: {result:.5f} з похибкою {error:.5e}")

# Оцінка точності
print(f"Відхилення Монте-Карло: {abs(area_estimate - result):.5f}")
