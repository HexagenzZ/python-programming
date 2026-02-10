# Set => kumpulan item bersifat unik, tanpa urutan (unordered collection)
# dapat diinitialize dengan {} dan juga setiap elementnya dipisahin sama koma
# nggak bisa indexing karena unordered

set = {1, 4, 5, 7, 3, 4, 5, "enam", "zetzz"}
print(set)
print(type(set))
# print(set[0])

# Selain dengan unordered / nggak beraturan index seperti list atau tuple
# Set juga data d dalamnya unik 
x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

# Set juga merupakan himpunan dalam matematika, kita bisa melakukan operasi
# Union 

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union :", union)

# Intersection
intersection = set1.intersection(set2)
print("Intersection :", intersection)
