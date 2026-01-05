import weakref

class Item:
    def __init__(self, name):
        self.name = name

item_collection = weakref.WeakSet()

# Menambahkan item ke koleksi
item1 = Item('Item 1')
item2 = Item('Item 2')
item_collection.add(item1)
item_collection.add(item2)

print("Koleksi item:", [item.name for item in item_collection])

del item1  # Hapus referensi kuat

print("Koleksi item setelah menghapus item1:", [item.name for item in item_collection])
# Fungsi: Mengelola koleksi objek menggunakan referensi lemah.
# Kondisi: Ketika Anda ingin menjaga data koleksi tanpa mencegah objek dihapus.
