import weakref

class MyClass:
    def __init__(self, value):
        self.value = value

# Membuat WeakSet
weak_set = weakref.WeakSet()

obj1 = MyClass(40)
obj2 = MyClass(50)

# Menambahkan objek ke WeakSet
weak_set.add(obj1)
weak_set.add(obj2)

print("Isi WeakSet:", [obj.value for obj in weak_set])  # Mengambil isi WeakSet

del obj1  # Menghapus referensi kuat

print("Isi WeakSet setelah menghapus obj1:", [obj.value for obj in weak_set])
# Fungsi: Mengelola koleksi objek menggunakan WeakSet.
# Kondisi: Ketika Anda ingin menyimpan objek dalam koleksi tanpa mencegah penghapusannya.
