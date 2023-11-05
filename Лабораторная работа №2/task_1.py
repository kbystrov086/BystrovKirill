money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост

month = 0

while True:
    dif = spend - salary
    if dif > money_capital:
        break
    month += 1
    money_capital -= dif
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", month)
