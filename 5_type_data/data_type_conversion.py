# hal yang dapat dilakukan selanjutnya pada tipe data ialah
# Konversi tipe data yaitu melakukan perubahan tipe data dari satu bentuk ke bentuk lainnya
# hal ini dapat dicapai dengan melakukan function ke tipe data tersebut

# Konversi integer ke Float
print(float(5))  # cukup masukkan fungsi float() dan masukkan int ke ()

# Konversi Float ke Integer
print(int(5.6))
print(int(-5.6))  # sama hal nya dengan float to int

# Konversi dari dan ke String
print(float("25"))
print(str(25.6))

# sama hal nya dengan data primitive data collection juga dapat dikonversi
print(set([1, 2, 3]))  # -> list ke set
print(tuple({5, 6, 7}))  # -> set ke tuple
print(list("hello"))  # -> string ke list

# seperti sebelumnya, cukup gunakan fungsi dengan tipe data konversi tujuan

# Konversi data ke dictionory
# untuk melakukan konversi ke dictionary, persyaratan key-vale harus terpenuhi
# Example :
# List dari beberapa list yang isinya psangan nilai menjadi dictionary
print(dict([[1, 2], [3, 4]]))

# konversi list dari beberapa tuple yang isinya pasangan nilai menjadi dictionary
print(dict([(3, 26), (23, 90)]))
