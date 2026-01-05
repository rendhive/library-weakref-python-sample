import weakref

class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(20)
weak_ref = weakref.ref(obj)

print("Sebelum menghapus:", weak_ref())  # Output: objek dengan nilai 20

del obj  # Menghapus referensi kuat

print("Setelah menghapus:", weak_ref())  # Output: None
# Fungsi: Memeriksa nilai dari referensi lemah setelah objek dihapus.
# Kondisi: Ketika Anda ingin melihat perilaku referensi lemah saat objek tidak ada lagi.
