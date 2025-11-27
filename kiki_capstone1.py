# ******************************
# SISTEM INVENTARIS ATK
# ******************************

inventaris = {
    "Pulpen": {"stok": 8,  "harga": 3000,  "minimal": 20},
    "Pensil": {"stok": 12, "harga": 2000,  "minimal": 25},
    "Penghapus": {"stok": 10,  "harga": 1500,  "minimal": 10},
    "Spidol": {"stok": 20,  "harga": 6000,  "minimal": 10},
    "Buku Tulis": {"stok": 43, "harga": 5000, "minimal": 30},
    "Stapler": {"stok": 17,  "harga": 25000,"minimal": 12},
    "Isi Stapler": {"stok": 121, "harga": 1000, "minimal": 80},
    "Map Plastik": {"stok": 34, "harga": 1500, "minimal": 50},
    "Kertas A4": {"stok": 587,"harga": 50,   "minimal": 500},
    "Lakban": {"stok": 10,  "harga": 8000, "minimal": 10},
    "Penggaris": {"stok": 17, "harga": 5000, "minimal": 15},
    "Correction Pen": {"stok": 7, "harga": 12000, "minimal": 10},
    "Clip Kertas": {"stok": 50, "harga": 200, "minimal": 100},
    "Binder": {"stok": 11, "harga": 2500, "minimal": 10},
    "Amplop": {"stok": 180, "harga": 500, "minimal": 100},
    "Label": {"stok": 30, "harga": 1000, "minimal": 50},
    "Tinta Printer": {"stok": 2, "harga": 150000, "minimal": 5},
    "Staples": {"stok": 199, "harga": 100, "minimal": 200},
    "Flashdisk": {"stok": 20, "harga": 120000, "minimal": 19},
    "Penghapus Spidol": {"stok": 21, "harga": 7000, "minimal": 15}
}

hapus_log = []  # log global, tempat hapus barang


# Fungsi Read Inventaris

def read_inventaris():
    print("\n=== DATA INVENTARIS ATK ===")
    print("{:<18} {:<8} {:<10} {:<8} {:<30}".format(
        "Barang", "Stok", "Harga", "Minimal", "Keterangan / Kekurangan"
    ))
    print("-" * 95)

    total_anggaran = 0
    for barang, data in inventaris.items():
        if data["stok"] < data["minimal"]:
            kekurangan = data["minimal"] - data["stok"]
            subtotal = kekurangan * data["harga"]
            total_anggaran += subtotal
            keterangan = f"STOK KURANG! Kekurangan: {kekurangan}, Rp -{subtotal}"
        else:
            keterangan = "Stok cukup!"
        print(f"{barang:<18} {data['stok']:<8} {data['harga']:<10} {data['minimal']:<8} {keterangan:<30}")

    print("-" * 95)
    print(f"{'TOTAL HARGA KEKURANGAN':<54} Rp {total_anggaran}\n")


# Fungsi Cari Barang

def cari_barang():
    cari = input("Cari barang (nama atau sebagian): ").strip().lower()
    if not cari:
        print("Tidak ada input pencarian.\n")
        return
    found_items = [(b, d) for b, d in inventaris.items() if cari in b.lower()]
    if found_items:
        print("\n=== Hasil Pencarian Barang ===")
        print("{:<18} {:<8} {:<10} {:<8}".format("Barang", "Stok", "Harga", "Minimal"))
        print("-"*50)
        for barang, data in found_items:
            print(f"{barang:<18} {data['stok']:<8} {data['harga']:<10} {data['minimal']:<8}")
        print()
    else:
        print("Barang tidak ditemukan.\n")


# Fungsi Tambah Barang

def create_barang():
    nama = input("Nama barang baru: ").strip()
    if nama in inventaris:
        print("Barang sudah ada!")
        return
    try:
        stok = int(input("Stok awal: "))
        harga = int(input("Harga satuan: "))
        minimal = int(input("Minimal stok: "))
    except ValueError:
        print("Input harus berupa angka!")
        return
    inventaris[nama] = {"stok": stok, "harga": harga, "minimal": minimal}
    print("Barang berhasil ditambahkan!\n")


# Fungsi Update Barang

def update_barang():
    print("\n=== Update Barang ===\nKosongkan input jika tidak ingin mengubah nilainya.")
    while True:
        nama = input("Nama barang yang ingin diupdate (ketik 'selesai' untuk berhenti): ").strip()
        if nama.lower() == "selesai":
            break
        if nama not in inventaris:
            print("Barang tidak ditemukan!")
            continue
        print(f"Barang: {nama} (Minimal stok: {inventaris[nama]['minimal']})")
        print("1. Update Stok & Harga")
        print("2. Rename Barang")
        opsi = input("Pilih opsi (1-2): ").strip()
        if opsi == "1":
            stok_input = input(f"Stok baru (sebelumnya {inventaris[nama]['stok']}): ").strip()
            if stok_input: inventaris[nama]["stok"] = int(stok_input)
            harga_input = input(f"Harga baru (sebelumnya {inventaris[nama]['harga']}): ").strip()
            if harga_input: inventaris[nama]["harga"] = int(harga_input)
        elif opsi == "2":
            baru = input("Nama baru: ").strip()
            if baru in inventaris: print("Nama barang baru sudah ada!"); continue
            inventaris[baru] = inventaris.pop(nama)
            nama = baru
            print(f"Barang berhasil diganti menjadi '{baru}'")
        else:
            print("Opsi tidak valid!"); continue
        status = "WARNING: Stok masih kurang!" if inventaris[nama]["stok"] < inventaris[nama]["minimal"] else "✔ Stok cukup."
        print(status + "\n")


# Fungsi Delete Barang + Undo

def delete_barang():
    print("\n=== HAPUS BARANG ===\nKetik nama barang satu per satu untuk dihapus. Ketik 'selesai' jika sudah selesai.\n")
    session_hapus = []
    while True:
        nama = input("Nama barang yang ingin dihapus: ").strip()
        if nama.lower() == "selesai": break
        if nama not in inventaris: print("Barang tidak ditemukan!\n"); continue
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus '{nama}'? (Y/N): ").strip().lower()
        if konfirmasi == "y":
            data = inventaris.pop(nama)
            hapus_log.append({nama: data})
            session_hapus.append({nama: data})
            print(f"Barang '{nama}' berhasil dihapus.\n")
    read_inventaris()
    if session_hapus or hapus_log:
        pilihan_undo = input(
            "Undo barang yang dihapus?\n1. Sesi terakhir\n2. Semua log\n3. Tidak\nPilihan (1-3): "
        ).strip()
        if pilihan_undo == "1":
            for item in session_hapus:
                for nama_k, data in item.items(): inventaris[nama_k] = data; print(f"Barang '{nama_k}' dikembalikan.")
            read_inventaris()
        elif pilihan_undo == "2":
            for item in hapus_log:
                for nama_k, data in item.items(): inventaris[nama_k] = data; print(f"Barang '{nama_k}' dikembalikan.")
            hapus_log.clear(); read_inventaris()
        else: print("Barang tetap terhapus.\n")

# ==============================
# Menu Utama

def menu():
    while True:
        print("\n" + "="*80)
        print("\033[1m" + "MENU SISTEM INVENTARIS ATK".center(80) + "\033[0m")
        print("="*80 + "\n")
        pilihan = input(
            "1. Lihat Inventaris\n"
            "2. Cari Barang\n"
            "3. Tambah Barang\n"
            "4. Update Barang\n"
            "5. Hapus Barang + Undo\n"
            "6. Keluar\n"
            "Pilih menu (1-6): "
        ).strip()
        if pilihan == "1": read_inventaris()
        elif pilihan == "2": cari_barang()
        elif pilihan == "3": create_barang()
        elif pilihan == "4": update_barang()
        elif pilihan == "5": delete_barang()
        elif pilihan == "6": print("Program selesai."); break
        else: print("Pilihan tidak valid!")

menu()
