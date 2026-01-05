import weakref

class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(10)

# Membuat referensi lemah
weak_ref = weakref.ref(obj)

print("Nilai melalui referensi lemah:", weak_ref() is not None)  # True
# Fungsi: Membuat referensi lemah yang mengarah ke objek.
# Kondisi: Ketika Anda ingin membuat referensi ke objek tanpa mencegahnya dihapus.
