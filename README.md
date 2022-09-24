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
       
       <div class='tableauPlaceholder' id='viz1664027978963' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Da&#47;DashboardGorontalosSelebgram&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='DashboardGorontalosSelebgram&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Da&#47;DashboardGorontalosSelebgram&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1664027978963');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='2450px';vizElement.style.width='100%';vizElement.style.minHeight='1387px';vizElement.style.maxHeight='2287px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='2450px';vizElement.style.width='100%';vizElement.style.minHeight='1387px';vizElement.style.maxHeight='2287px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='2227px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
