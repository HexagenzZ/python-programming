# Now is, tipe data collection
# tipe data collection adalah tipe data yang menyimpan satu atai lebih data primitif sebagai satu kelompok

# I. List
# => jenis kumpulan data terurut(ordered sequence)
# => serupa tapi tak sama dengan array pada other language, 
# tidak mengharuskan tipe data yang sama dalam kelompoknya, array sebaliknya

# untuk membuat list hanya perlu [] dan juga , (koma) di antara character
list = [1, 2.34, "BOOST", True]
print(list)
print(type(list))

# Setiap char di list itu ada indexnya, index dimulai dari 0, dan bisa akses list pakai indexing
print(list[2])

# List pada python itu mutable, dalam artian bisa diubah isinya
list[0] = "Tokyo"
print(list)


### indexing
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])

### slicing 
# => slicing merujuk pada pengambilan data berdasarkan indeks dari rentang tertentu.
# => format untuk slicing = sequence[start:stop:step]
print(x[0:5:2])
print(x[1:])
print(x[:3])
