# Declare itu merujuk pada pemberian tipe data pada variabel yang bakal dibuat
# Example :

"""
int age ;
float salary ;
string name ;
"""

# kalau Initialize itu sama dengan pemberian nilai awal untuk suatu variabel yang sudah di declare
# Example :

"""
int age = 19 ;
float salary = 1200000.0 ;
string name = mulyono ;
"""

# Hal-hal di atas itu wajib di beberapa bahasa pemrograman, conotoh: c++, java, dll
# Python termasuk loosely typed, jadi nggak perlu buat declare
# loosely typed = tipe bahasa pemrograman yang nggak perlu declare type data secara explisit

age = 19
salary = 500000.000

print(type(age))
print(type(salary))

# python juga dynamic typing => programming language yang tau secara langsung tipe data waktu programnya dijalanin

x = 7
print(type(x))

x ="7"
print(type(x))
