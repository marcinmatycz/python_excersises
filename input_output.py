
# zapis

data_write = input("Dane do wpisania: ")
f = open("data.txt", "w+")
f.write(data_write)
f.close()

# odczyt

f = open("data.txt", "r+")
data_read = f.read()
print(data_read)