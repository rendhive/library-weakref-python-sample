import weakref

class MyClass:
    def __init__(self, value):
        self.value = value

def callback(reference):
    print(f"Objek dengan nilai {reference} telah dihapus")

obj = MyClass(30)
weak_ref = weakref.ref(obj, callback)

print("Sebelum menghapus:", weak_ref())

del obj  # Menghapus referensi kuat
# Fungsi: Menyediakan callback yang dipanggil saat objek dihapus.
# Kondisi: Ketika Anda ingin melakukan tindakan tertentu saat objek tidak ada lagi.
