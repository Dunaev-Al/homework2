old_rates = [7, 5, 3, 3, 2]
new_rates = []
user_number = int(input('Введите число для рейтинга'))


for i in range(0,len(old_rates)):
    if int(old_rates[i]) >= user_number:
        new_rates.append(old_rates[i])
    else:
        new_rates.append(user_number)
        for index in range(i, len(old_rates)):
            new_rates.append(old_rates[index])
        break

old_rates = new_rates
print(old_rates)



