**SISTEM INVENTARIS ATK**

Program Sistem Inventaris ATK ini merupakan aplikasi berbasis terminal untuk mengelola data inventaris, seperti nama barang, stok, harga, dan batas stok minimal. Sistem ini dirancang sederhana namun memiliki struktur yang jelas sehingga mudah dipelajari, dimodifikasi, dan digunakan sebagai contoh manajemen data menggunakan Python.

**Tujuan Program**

Program ini dibuat untuk:

- Mengelola inventaris alat tulis atau barang lainnya secara terstruktur.
- Mempermudah pencatatan informasi seperti stok, harga, dan batas minimal.
- Memberikan peringatan otomatis ketika stok berada di bawah batas minimal.
- Melatih pemahaman konsep dasar pemrograman seperti struktur data, fungsi, percabangan, perulangan, validasi input, dan penanganan kesalahan.

**Struktur Penyimpanan Data**

Data inventaris disimpan menggunakan struktur dictionary bersarang.\
Setiap barang memiliki tiga atribut utama:

- Stok barang
- Harga barang
- Minimal stok sebelum dianggap kekurangan

Nama barang digunakan sebagai indeks utama sehingga setiap barang bersifat unik dalam penyimpanan.

**Alur Kerja Program**

1. Pengguna masuk ke menu utama.
1. Program menampilkan beberapa pilihan menu.
1. Pengguna memilih menu tertentu seperti menambah, menghapus, mengedit, atau melihat data.
1. Program menjalankan fungsi sesuai pilihan.
1. Setelah selesai, program kembali ke menu utama hingga pengguna memilih keluar.

Alur ini berputar menggunakan perulangan sehingga pemakaian dapat berlanjut tanpa memulai ulang program.

**Penjelasan Menu dan Fitur**

**1. Tambah Barang**

Menu ini digunakan untuk menambahkan data baru ke inventaris.\
Pengguna diminta memasukkan:

- Nama barang
- Stok awal
- Harga barang
- Stok minimal

Jika nama barang belum ada, data baru ditambahkan dan dikonfirmasi berhasil.\
Jika nama barang sudah ada, pengguna diminta mengganti nama agar tidak terjadi duplikasi.

**2. Hapus Barang**

Pengguna dapat menghapus satu atau lebih barang dengan memasukkan nama barang yang ingin dihapus.\
Program akan:

1. Memeriksa apakah barang ada dalam inventaris.
1. Menghapus data barang jika ditemukan.
1. Menyimpan data barang yang dihapus ke dalam log untuk keperluan undo.
1. Menampilkan data terbaru setelah penghapusan.
1. Menawarkan pilihan kepada pengguna untuk mengembalikan data yang terhapus:
   1. Undo hanya yang dihapus pada sesi terakhir
   1. Mengembalikan seluruh data yang pernah dihapus
   1. Tidak melakukan undo

Fitur ini mencegah penghapusan permanen yang tidak disengaja.

**3. Edit Barang**

Menu ini memiliki dua opsi pengeditan utama.

**Opsi 1: Mengubah stok dan/atau harga**

Pengguna dapat memperbarui:

- Stok barang
- Harga barang

Pengguna boleh memasukkan hanya salah satu dari keduanya.\
Jika input dikosongkan, nilai sebelumnya akan dipertahankan.

Setelah perubahan dilakukan, program menampilkan status stok:

- Peringatan jika stok masih kurang dari minimal
- Informasi stok cukup jika memenuhi batas

**Opsi 2: Mengganti nama barang**

Pengguna dapat mengganti nama barang dengan nama baru selama nama baru belum digunakan oleh barang lain.\
Seluruh data sebelumnya dipindahkan ke nama baru secara otomatis.

**4. Tampilkan Inventaris**

Menu ini menampilkan seluruh barang dalam format tabel berisi:

- Nama barang
- Stok
- Harga
- Minimal stok
- Status ketersediaan (cukup atau kurang)

Selain itu, ditampilkan:

- Total anggaran yang diperlukan untuk menutupi kekurangan stok\
  (yaitu selisih stok minimal dan stok saat ini dikalikan harga)

Menu ini juga memungkinkan pencarian barang tertentu berdasarkan kata kunci, menampilkan satu baris detail barang yang dicari beserta posisinya dalam tabel.

**5. Keluar Program**

Program berhenti dan pengguna keluar dari aplikasi.

**Penjelasan Teknis**

**Penggunaan Return**

Return digunakan untuk mengakhiri fungsi lebih awal apabila:

- Input tidak valid
- Barang tidak ditemukan
- Proses tidak perlu dilanjutkan

Return membantu menjaga agar alur program tetap bersih dan tidak mengeksekusi kode yang tidak relevan.

**Penggunaan Continue**

Continue digunakan di dalam perulangan menu untuk:

- Melewati proses yang tidak perlu
- Mengulang menu tanpa keluar dari loop

Penggunaan ini penting saat input tidak valid atau pengguna perlu mengulangi pilihan tanpa mengganggu logika utama.

**Pencarian Barang**

Pencarian dilakukan dengan mencocokkan kata kunci dengan nama barang.\
Program hanya mencari pada bagian key (nama barang), bukan pada atribut di dalamnya.

Hasil pencarian ditampilkan dalam format tabel untuk memudahkan identifikasi.

**Penutup**

Program ini menjadi contoh lengkap bagaimana membangun sistem CRUD (Create, Read, Update, Delete) berbasis terminal dengan tambahan fitur seperti pencarian, validasi input, undo penghapusan, dan perhitungan anggaran.

