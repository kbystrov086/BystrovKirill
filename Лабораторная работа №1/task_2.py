pages = 100
lines = 50
chars = 25
trans_chars = 4
translate = 1024
volume = 1.44

total_chars = pages * lines * chars
total_bytes = total_chars * trans_chars

disk_size = volume * translate * translate
result = int(disk_size // total_bytes)

print("Количество книг, помещающихся на дискету:", result)
