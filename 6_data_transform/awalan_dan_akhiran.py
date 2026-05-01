# transformasi yang dilakukan pada hal ini adalah menghilangkan beberapa karakter yang tidak diinginkan dalam suatu kalimat
# biasanya dilakukan untuk whitepace (spasi berlebihan yang tidak diinginkan)
# selain whitespace bisa juga dilakukan pada kalimat" yang tidak diinginkan

# rstrip()
# => menghapus karakter yang berada pada sebelah kanan ataupun skhir dari string
# Example :
print("Hogwarts                   ".rstrip() + " Legacy")

# ltsrip()
# => kebalikan dari yang sebelumnya, method ini ngambil yang kiri ataupun awal string
# Example :
print("       Gryffindor".lstrip())

# strip()
# => bisa manghapus karakter yang berada di awal ataupun akhir
# Example :
print("          Ravenclaw           ".strip())

# => bisa dilakukan pada selain whitespace
# Example :
sly = "HogHogHogSlytherinHogHog"
print(sly.strip("Hog"))

# method sebelumnya adalh penghapusan, sekarang pencarian
# startswith()
# => bertujuan menemukan kata yang diawali dengan kata yang hendak dicari, method mengembalikan nilai true
# Example :
print("Hogwarts is Crazy".startswith("Hogwarts"))
print("Hogwarts is Crazy".startswith("Crazy"))

# endswith()
# => kebalikan dari startswith, True jika akhiran sama dengan hal yang dicari
# Example :
print("Hagrid is Hufflepuff".endswith("Hufflepuff"))
