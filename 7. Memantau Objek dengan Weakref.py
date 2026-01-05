import weakref

class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(60)

# Membuat weak reference
weak_ref = weakref.ref(obj)

print("Nilai objek:", weak_ref().value)

del obj  # Menghapus referensi kuat

# Memantau objek
if weak_ref() is None:
    print("Referensi lemah tidak lagi ada.")
# Fungsi: Memantau keberadaan objek menggunakan referensi lemah.
# Kondisi: Ketika Anda ingin memeriksa apakah objek masih hidup tanpa mencegah penghapusannya.
