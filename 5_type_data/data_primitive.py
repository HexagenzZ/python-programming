"""
Tipe data itu terbagi jadi dua, ada primitive ada collection
tipe data primitive itu nyimpan single value, contoh "var = 4"
"""
# I. tipe data number 
# terdapat 3 tipe data number => integer, flaot, complex
# integer = angka bulat yang positif dan negatif, dalam artian nggak ada desimal
# float = bilangan riil yang mewakili bilangan bulat dan desimal
# complex = bilangan complex kaya 2y, dll

# Ciri tipe data number itu bisa dilakukan operasi data
x = 6
print(type(x))

flt = 23.4
print(type(flt))

y = 1+2j
print(type(y))

# Tipe data number itu immutable = tidak bisa diubah
varz = 10
print(varz)
print(id(varz))

varz = 11
print(varz)
print(id(varz))

# jika dilihat dari output di atas, yang mana kita sudah membuat variable dengan nama yang sama
# alokasi memorinya tetapi beda yang membuktikan bahwa number = immutable, namun jika value
# pada variable disamakan maka dilihat pada output hasil alokasi memoriny sama

# II. tipe data boolean
# tipe data yang hanya berisi nilai TRUE dan FALSE
# semua tipe data yang diisi itu bernilai TRUE
# bernilai FALSE dalam beberapa keadaan, di antaranya:
# nilai yang sudah didefinisikan NONE dan FALSE
# angka nol dari semua tipe data numerik
# tipe data sequence dan collection yang isinya masih kosong

x = True
print(type(x))

x = False
print(type(x))
print(bool(x))

zero = 0
print(bool(zero))

array = {}
print(bool(array))

# III. Tipe data string
# ini itu isinya selain yang dua tadi, tapi tetep bisa masuk" aja sih yang dua tadi
# singkatnya isinya itu char, (emoji bisa, angka bisa) dll
# tandanya ya di apit single quote atau double quote

x = "Itadakimasu"
print(type(x))

## beberapa keunikan string :
# bisa simpan string yang multiline dengan tiga single quote atau double quote 
var1 = '''
Tokito Muichiro
Mist Hashira
'''

print(var1)

var2 = """
Limitless
Infinity
"""

print(var2)

# string itu indeks, jadi bisa akses beberapa character dalam string dengan cara indexing
index = "Megagamma"
print(index[5])

# meskipun bisa di akses tetapi, string juga mutable, dalam artian tidak bisa diubah
axel = "Driver DND"
# axel[0] = "7"

# selain bisa di akses dengan indexing, juga bisa akses beberapa substring pakai method slicing dan indexing
X = "Geizzz"
print(X[3:])

# dapat menampilkan string yang dinputkan oleh user:, terdapat beberapa cara di antaranya:
## FORMATTED STRING
name = "Harry Potter"
print(f"My Name is {name}")

## FORMATTING
name = "Ron Weasley"
print("Oh, Hello Harry, My Name is %s" %(name))

## str.format
name = "Hermione Granger"
print("I am {}".format(name))

