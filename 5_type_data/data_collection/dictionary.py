# Dictionary => merupakan tipe data kumpulan pasangan key-value yang sifatnya tidak berurutan
# Didefinisikan dengan kurung kurawal {}, dan juga dengan bbrapa tambahan definisi berikut :
# 1. setiap elemen pasangan key-value dipisahkan dengan koma {}
# 2. key dan value dipisahkan dengan : {}
# 3. key dan value dapat berupa variabel dan objek apapun {}

# Example :
x = {"name": "Draco Malfoy", "age": 14, "isMarried": True}
print(x)
print(type(x))

# untuk mengakses sebuah value dalam dictionary, harus diketahui key nya terlebih dahulu
# hal ini berbeda dengan tipe data collection lainnya yang mana cukup menyebutkan indexnya saja, kecuali tuple
# Example
# print(x[0])

# cara akses dictionary yang benar adalah seperti ini
print(x["name"])

# beberapa hal yang bisa dilakukan di dictionary antara lain :
# I. menambahkan data di dictionary
bio = {"name": "Helga Hufflepuff", "age": 25, "isMarried": False}
bio["job"] = "Witch"  # berikut cara menambahkan datanya
print(bio)

# II. menghapus data pada dictionary
deldict = {"name": "Cedric Diggory", "age": 17, "isMarried": False}
del deldict["isMarried"]  # cukup tambahan "del" dengan metode berikut
print(deldict)

# III. mengubah data pada dictionary
edited = {"name": "Lucius Malfoy", "age": 44, "isMarried": False}
edited["isMarried"] = True
print(edited)
