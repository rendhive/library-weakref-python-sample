import weakref

class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

obj = MyClass(70)
weak_method = weakref.WeakMethod(obj.display)

strong_ref = obj.display  # Referensi kuat ke metode

# Memanggil metode dengan referensi lemah
if weak_method() is not None:
    weak_method()()
else:
    print("Metode tidak dapat diakses.")

del obj  # Hapus referensi kuat

# Memanggil setelah menghapus objek
if weak_method() is not None:
    weak_method()()
else:
    print("Metode tidak dapat diakses.")
# Fungsi: Mengakses metode objek menggunakan weak reference.
# Kondisi: Ketika Anda ingin membuat referensi lemah ke metode sehingga objek tidak terikat.
