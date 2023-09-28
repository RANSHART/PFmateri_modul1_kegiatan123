random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

int_dict = {}  # Untuk menyimpan nilai integer
float_tuple = ()  # Untuk menyimpan nilai float
str_list = []  # Untuk menyimpan nilai string

for item in random_list:
    if isinstance(item, int):
        # Memisahkan angka satuan, puluhan, dan ratusan
        units = item % 10
        tens = (item // 10) % 10
        hundreds = item // 100

        int_dict[item] = (hundreds, tens, units)
    elif isinstance(item, float):
        float_tuple += (item,)
    elif isinstance(item, str):
        str_list.append(item)

print("Nilai Integer dalam Dictionary:")
print(int_dict)

print("Nilai Float dalam Tuple:")
print(float_tuple)

print("Nilai String dalam List:")
print(str_list)
