item1 = {"nama": "Rokok", "stok":10, "harga":100}
item2 = {"nama": "Asbak", "stok":14, "harga":352}
item3 = {"nama": "Kacamata", "stok":12, "harga":231}
item4 = {"nama": "Garpu", "stok":32, "harga":50}
item5 = {"nama": "Kompor", "stok":51, "harga":400}

items = [item1, item2, item3, item4, item5]

for i in range(len(items)):
    print("Ada", items[i]["nama"],"Dengan stok berjumlah:",items[i]["stok"],"dan harganya adalah:",items[i]["harga"])

nama = input("Nama barang: ")
stok = input("Berapa stok yang ingin ditambahkan?: ")
harga = input("Berapa harganya?: ")

items6 = {"nama":nama, "stok":stok, "harga":harga}
items.append(items6)
print(f"Barang dengan nama({items6['nama']})","Berhasil ditambahkan.")
for j in range(len(items)):
    print("Ada", items[j]["nama"],"Dengan stok berjumlah:",items[j]["stok"],"dan harganya adalah:",items[j]["harga"])
print("Selesai")


