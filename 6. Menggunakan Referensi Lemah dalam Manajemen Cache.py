import weakref

class Data:
    def __init__(self, value):
        self.value = value

cache = {}

def get_data(value):
    if value not in cache:
        data = Data(value)
        cache[value] = weakref.ref(data)
    return cache[value]() 

data1 = get_data(100)
print("Data 100:", data1.value)

del data1  # Hapus referensi kuat

print("Data 100 setelah dihapus:", get_data(100))  # Akan membuat objek baru
# Fungsi: Mengelola cache menggunakan referensi lemah untuk penyimpanan data ringan.
# Kondisi: Ketika Anda ingin membatasi penggunaan memori dengan cache yang efisien.
