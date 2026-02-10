# Tuple => jenis list tetapi datanya immutable, dalam artian, tidak dapat diubah.
# untuk mendefinisikan tuplle itu dengan tutup kurung (), dan juga koma di setiap char

tuple = ("mecha", "plasma", "shadow", 7, 9, 8, True)
print(tuple)
print(type(tuple))

'''
Sama sepert list, tuple bisa juga dilauka indexing dan slicing
'''

print(tuple[1]) # Indexing
print(tuple[0:4]) # Slicing

# Seperti yang disebutkan sebelumnya, tuple itu immutable
test = (9, 0, False, 'Archiball')
# test[2] = True
