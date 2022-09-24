# Scraping Data Instagram 
## 1. Deskripsi
Repositori ini berisi script untuk mendownload data dari instagram. Data yang dapat didownload antara lain:
  1. ID postingan
  2. Nama akun pengguna
  3. Nama lengkap pada akun
  4. Jumlah followers
  5. Jenis postingan
  6. Waktu postingan
  7. Test pada postingan
  8. Jumlah Like
  9. Jumlah Komentar
  10. Jumlah viewer jika postingan dalam bentuk video
  11. URL postingan
  
## 2 Cara Penggunaan
 Untuk dapat mendownload data dari instagram menggunakan script di dalam repositori ini dapat mengikuti langkah-langkah berikut:
#### 2.1 Mendowload repository ke komputer lokal
           Untuk mendownload dapat dilakukan dengan klik tombol **code** dibagian kanan atas repository kemudian klik tombol **Download Zip**. Cara lain dapat menggunakan perintah di git `git pull https://github.com/Muhammadfaizaladdi/scraping_instagram_data.git`
  
#### 2.2 Membuat virtual environment
           Jika tidak ingin menginstall modul yang dibutuhkan oleh repository ini ke komputer lokal, dapat menggunakan virtual env. Untuk membuatnya, eksekusi perintah `python -m venv nama_virtual_environment` pada terminal. Kemudian pindahkan semua file yang ada di repository yang telah di download ke dalam virtual environment.
  
#### 2.3 Membuat file variabel configurasi yang dibutuhkan
           Terdapat beberapa variabel yang dibutuhkan untuk menjalankan script ini. yaitu:
           - user : nama akun yang dapat digunakan untuk login ke instagram
           - pswd : password dari nama akun yang akan digunakan untuk login
           - user_name : daftar nama akun yang akan diakses datanya (dalam bentuk list)
           - initial_path : digunakan untuk management direktori saat menjalankan script
           
           Variabel-variabel tersebut disimpan kedalam file **variables.yaml**
           
#### 2.4 Buat folder data
           Hasil scraping akan disimpan didalam folder bernama **data**. Oleh karena itu buat folder data di dalam folder virtual environment.
#### 2.5 Install dependensi
           Untuk menginstall semuda dependensi, arahkan kursor di terminal ke dalam folder virtual environment yang dibuat, kemudian jalankan perintah `pip install -r requirements.txt`
#### 2.6 Ganti nama file output (opsional)
           Jika ingin menggunakan nama file output yang spesifik, rubah nilai variabel `saved_filename` pada file `run.py`
           
  Setelah menjalankan langkah-langkah diatas, file hasil scraping akan disimpan didalam folder data sesuai dengan nama yang telah ditentukan.
  
## 3 Analisis Data
       Setelah mendownloadnya anda dapat menlanjutkan ke tahapan cleaning atau analisis
       Contoh hasil analisis dari data yang telah di dapatkan:   
       https://public.tableau.com/views/DashboardGorontalosSelebgram/Dashboard1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link
