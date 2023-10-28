numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

skip_none1 = numbers[5:]
skip_none2 = numbers[:4]
skip_none = skip_none2 + skip_none1

avarage = sum(skip_none)/len(numbers)
numbers[4] = avarage
print("Измененный список:", numbers)
