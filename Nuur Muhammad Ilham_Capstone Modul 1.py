from tabulate import tabulate # Untuk membuat tampilan tabel menjadi lebih rapih 

# Database mobil rental
# Tipe koleksi data dictionary dalam list
# ID dibuat berdasarkan maping dari merk, tipe, transmisi, dan nomor urut data
rental_car = [
    {'ID': 11201, 'merk': 'Daihatsu', 'tipe': 'Xenia', 'plat' : 'B 1234 ABC', 'seats': 7, 'bahan_bakar': 'Bensin', 'transmisi': 'Manual', 'status': 'Tersedia', 'harga': 200000},
    {'ID': 21101, 'merk': 'Honda', 'tipe': 'Brio', 'plat' : 'B 9876 XYZ', 'seats': 5, 'bahan_bakar': 'Bensin', 'transmisi': 'Automatic', 'status': 'Disewakan', 'harga': 300000},
    {'ID': 31201, 'merk': 'Toyota', 'tipe': 'Yaris', 'plat' : 'B 321 DEF' , 'seats': 5, 'bahan_bakar': 'Bensin', 'transmisi': 'Manual', 'status': 'Maintenance', 'harga': 350000},
    {'ID': 41101, 'merk': 'Mitsubishi', 'tipe': 'Xpander', 'plat' : 'B 567 GHI', 'seats': 7, 'bahan_bakar': 'Bensin', 'transmisi': 'Automatic', 'status': 'Tersedia', 'harga': 400000},
    {'ID': 32201, 'merk': 'Toyota', 'tipe': 'Innova', 'plat' : 'B 8765 MNO', 'seats': 7, 'bahan_bakar': 'Diesel', 'transmisi': 'Manual', 'status': 'Disewakan', 'harga': 850000},
    {'ID': 51101, 'merk': 'Wuling', 'tipe': 'Air Ev', 'plat' : 'B 2345 JKL', 'seats': 4, 'bahan_bakar': 'Electric', 'transmisi': 'Automatic', 'status': 'Maintenance', 'harga': 550000}
    ]

# Mapping untuk merk, tipe, dan transmisi menggunakan angka(integer)
merk_map = {'Daihatsu': 1, 'Honda': 2, 'Toyota': 3, 'Mitsubishi': 4, 'Wuling': 5}
tipe_map = {'Xenia': 1, 'Brio': 1, 'Yaris': 1, 'Xpander': 1, 'Innova': 2, 'Air Ev': 1}
transmisi_map = {'Automatic': 1, 'Manual': 2}

### Fungsi Menampilkan Daftar Mobil ###
def show_car_list(data):
    if len(data) == 0:
        print('Data tidak tersedia') # Memeriksa jika data tidak ada maka pesan akan muncul
        return
    tabel_data = []
    for car in data:
        tabel_data.append([car['ID'], car['merk'], car['tipe'], car['seats'], car['plat'], car['bahan_bakar'], car['transmisi'], car['status'], car['harga']])
    headers = ['ID', 'Merk', 'Tipe', 'Seats', 'Plat_Mobil', 'Bahan_Bakar', 'Transmisi', 'Status', 'Per_Hari_(Rp)']
    print(tabulate(tabel_data, headers, tablefmt='pretty', stralign='center', numalign='center'))

### Fungsi Membuat ID Mobil ###
def generate_id(merk, tipe, transmisi, data):
    # Mengambil kode integer untuk merk, tipe, dan transmisi dari mapping yang sudah ditentukan
    merk_part = merk_map[merk] # Mengambil nilai dari maping berdasarkan key merk
    tipe_part = tipe_map[tipe] # Mengambil nilai dari maping berdasarkan key tipe
    transmisi_part = transmisi_map[transmisi] #Mengambil nilai dari maping berdasarkan key transmisi
    nomor_urut = 1 # Memulai nomor urut dari 1
    id_unik = int(f"{merk_part}{tipe_part}{transmisi_part}{nomor_urut:02d}") # Membuat ID unik dengan format integer
    id_list = [car['ID'] for car in data] # Loop untuk memeriksa apakah terdapat ID sama
    # Loop untuk memastikan ID menjadi unik
    while id_unik in id_list:
        nomor_urut += 1  # Jika ID sudah ada akan di tambahkan 1 sebagai pembeda
        id_unik = int(f"{merk_part}{tipe_part}{transmisi_part}{nomor_urut:02d}") # Bentuk ID baru dengan nomor urut yang baru ditambahkan
    return id_unik 

### Fungsi Menampilkan Mobil Berdasarkan ID ###
def car_by_id(data):
    id_mobil = input('Masukkan ID Mobil : ')
    if not id_mobil.isdigit(): # Memeriksa inputan apakah hanya angka
        print('Pilihan tidak valid') # Jika inputan tidak sesuai maka pesan akan muncul
        return 
    id_mobil = int(id_mobil)
    if len(data) == 0:
        print('Data tidak tersedia')
        return 
    for car in data:
        if car['ID'] == id_mobil:
            tabel_data = [[car['ID'], car['merk'], car['tipe'], car['seats'], car['plat'], car['bahan_bakar'], car['transmisi'], car['status'], car['harga']]]
            headers = ['ID', 'Merk', 'Tipe', 'Seats', 'Plat_Mobil', 'Bahan_Bakar', 'Transmisi', 'Status', 'Per_Hari_(Rp)']
            print(tabulate(tabel_data, headers, tablefmt='pretty', stralign='center', numalign='center'))
            return car
    print(f'Data tidak tersedia dengan ID {id_mobil}')
    return

### Fungsi Input Harga Minimum dan Maksimum ###
def input_harga_min_max():
    while True:
        harga_min = input('Masukkan harga minimum : ')
        if harga_min.isdigit() and len(harga_min) >= 4 and harga_min[-4:] == '0000' and int(harga_min) > 199999: # Memastikan inputan angka and 4 angka terakhir harus 0 dan minimal 200000
            harga_min = int(harga_min)
            break
        else:
            print('''Inputan tidak valid. inputan hanya angka, minimal 200000,
                dan 4 angka terakhir harus 0 (Contoh 250000)''')
    while True:
        harga_max = input('Masukkan harga maksimum: ')
        if harga_max.isdigit() and len(harga_max) >= 4 and harga_max[-4:] == '0000' and int(harga_max) > harga_min: # Memastikan inputan angka and 4 angka terakhir harus 0 dan harus lebih besar dari inputan harga minimum
            harga_max = int(harga_max)
            return harga_min, harga_max
        else:
            print('''Inputan tidak valid. Harga maksimum harus lebih besar dari harga minimum, 
            inputan harus angka, dan 4 angka terakhir harus 0 (Contoh 250000)''')

### Fungsi Filter Mobil Berdasarkan Transmisi dan Harga ###
def filter_transmisi_harga(data):
    if len(data) == 0:
        print('Data tidak tersedia') # Jika data kosong akan menampilkan pesan 
        return
    transmisi = input_transmisi() 
    harga_min, harga_max = input_harga_min_max()  # Memanggil fungsi inpun harga min dan max lalu di simpan dalam variabel harga min dan max
    filtered_data = [] # Inisiasi tabel untuk menyimpan data mobil 
    for car in data: # Melakukan iterasi pada setiap mobil di data
        if car['transmisi'] == transmisi and harga_min <= car['harga'] <= harga_max: # Memeriksa apakah transmisi mobil sesuai degnan rentang yang diinginkan
            filtered_data.append(car) # Menambahkan mobil yang sesuai ke list filtered_data
    if not filtered_data: # Menambahkan mobil yang sesuai ke list filtered_data
        print(f'Tidak ada mobil dengan transmisi {transmisi} dan harga antara {harga_min} dan {harga_max}')
        return
    tabel_data = []
    for car in filtered_data: # Mengisi tabel_ ata dengan data dari filtered data
        tabel_data.append([car['ID'], car['merk'], car['tipe'], car['seats'], car['plat'], car['bahan_bakar'], car['transmisi'], car['status'], car['harga']])
    headers = ['ID', 'Merk', 'Tipe', 'Seats', 'Plat_Mobil', 'Bahan_Bakar', 'Transmisi', 'Status', 'Per_Hari_(Rp)'] # Membuat header tabel
    print(tabulate(tabel_data, headers, tablefmt='pretty', stralign='center', numalign='center')) # Menampilkan data sesuai dengan posisi tengah

### Fungsi Validasi Ya atau Tidak ###
def validasi_yes_no():
    while True:
        confirm = input('Apakah anda yakin ingin melanjutkan? (Y/T) : ').upper()
        if confirm in ['Y','T']:
            return confirm
        else:
            print('Inputan tidak valid. Sillahkan masukkan Y atau T')

### Fungsi Input Merk Mobil ###
def input_merk():
    while True:
        merk = input('Masukkan Merek Mobil: ').title()
        if all(char.isalpha() or char.isspace() for char in merk): # Memeriksa inputan apakah hanya huruf dan apakah terdapat spasi
            if merk in merk_map:
                return merk
            else:
                print('Merk tidak terdaftar dalam peta merk')
        else:
            print('Inputan tidak valid. Masukkan merek tanpa angka')

### Fungsi Input Tipe Mobil ###
def input_tipe():
    while True:
        tipe = input('Masukkan Tipe Mobil: ').title()
        if all(char.isalpha() or char.isspace() or char.isdigit() for char in tipe): # Memeriksa inputan apakah hanya huruf, terdapat spasi, dan terdapat angka
            if tipe in tipe_map:
                return tipe
            else:
                print('Tipe tidak terdaftar dalam peta tipe')
        else:
            print('Inputan tidak valid')

### Fungsi Input Jumlah Seats Mobil ###
def input_seats():
    while True:
        seats = input('Masukkan Jumlah Seat Mobil (4, 5, 7) : ')
        if seats.isdigit() and int(seats) in [4, 5, 7]: # Memeriksa inputan hanya angka dan di batasi hanya pada angka 4,5,7 saja
            return int(seats)
        else:
            print('Inputan tidak valid. Silahkan memasukkan 4, 5, atau 7')

### Fungsi Input Plat Nomor Mobil ###
def input_plat():
    while True:
        print('''Masukkan plat nomor mobil dengan format AA BBBB CCC (B 1907 LH)\n
        AA   = Huruf bagian depan mobil (Maksimal 2 huruf)
        BBBB = Angka pada plat mobil (Maksimal 4 angka dan angka pertama tidak boleh 0)
        CCC  = Huruf bagian akhir pada plat mobil (Maksimal 3 huruf)\n''')
        plat = input('Masukkan Nomor Plat Mobil : ').upper() 
        nomor = plat.split()
        # Memeriksa apakah format plat nomor terdiri dari 3 bagian
        if (len(nomor) == 3 and
            # Memeriksa apakah bagian pertama maksimal 2 huruf dan hanya berisi huruf
            len(nomor[0]) <= 2 and nomor[0].isalpha() 
            # Memeriksa apakah bagian kedua maksimal 4 angka, bagian pertama tidak boleh nol, dan hanya berisi angka
            and nomor[1].isdigit() and 1 <= len(nomor[1]) <= 4 and nomor[1][0] != '0' 
            # Memeriksa apakah bagian ketiga maksimal 3 huruf dan hanya berisi huruf
            and 1 <= len(nomor[2]) <= 3 and nomor[2].isalpha()):
            # Jika semua kondisi terpenuhi, mengembalikan plat nomor yang valid
            return plat
        else:
            print('Inputan tidak valid. Masukkan plat seusai dengan format\n')

### Fungsi Input Bahan Bakar Mobil ###
def input_bahan_bakar():
    while True:
        bahan_bakar = input('''Masukkan Jenis Bahan Bakar 
                1. Bensin
                2. Diesel
                3. Electric
        Masukkan pilihan anda: ''')
        # Memeriksa apakah input adalah digit dan dalam rentang 1-3
        if bahan_bakar.isdigit() and int(bahan_bakar) in range(1, 4):
            # Mengembalikan jenis bahan bakar berdasarkan input
            if bahan_bakar == '1':
                return 'Bensin' # Jika inputan 1 maka akan di ubah menjadi bensin
            elif bahan_bakar == '2':
                return 'Diesel'  # Jika inputan 2 maka akan di ubah menjadi diesel
            elif bahan_bakar == '3':
                return 'Electric'  # Jika inputan 3 maka akan di ubah menjadi electric
        else:
            # Menampilkan pesan kesalahan jika input tidak valid
            print('Inputan yang anda masukkan tidak tersedia pada pilihan')

### Fungsi Input Transmisi Mobil ###
def input_transmisi():
    while True:
        transmisi = input('''Masukkan Transmisi 
                1. Automatic
                2. Manual
        Masukkan pilian anda: ''')
        if transmisi.isdigit() and int(transmisi) in range(1, 3):
            if transmisi == '1':
                return 'Automatic' # Jika inputan 1 maka akan di ubah menjadi automatic
            elif transmisi == '2':
                return 'Manual' # Jika inputan 2 maka akan di ubah menjadi manual
            break
        else:
            print('Inputan yang anda masukkan tidak tersedia pada pilihan')

### Fungsi Input Status Mobil ###
def input_status():
    while True: 
        status_input = input('''Masukkan status 
                1. Tersedia
                2. Disewakan
                3. Maintenance
        Masukkan pilihan anda : ''')
        if status_input.isdigit() and int(status_input) in range(1, 4):
            if status_input == '1':
                return 'Tersedia' # Jika inputan 1 maka akan di ubah menjadi tersedia
            elif status_input == '2':
                return 'Disewakan' # Jika inputan 2 maka akan di ubah menjadi disewakan
            elif status_input == '3':
                return 'Mainntenance' # Jika inputan 3 maka akan di ubah menjadi maintenance
        else:
            print('Inputan yang anda masukkan tidak tersedia pada pilihan')

### Fungsi Input Harga Mobil ###
def input_harga():
    while True:
        harga = input('Masukkan Harga Sewa : ')
        if harga.isdigit() and len(harga) >= 4 and harga[-4:] == '0000' and int(harga)> 199999: # Memeriksa apakah inputan hanya angka, 4 digit di belakang 0, dan inputan minimal 200000
                return int(harga)
        else:
            print('''Inputan tidak valid. Silakan masukkan hanya angka, minimal 200000, 
                    dan 4 angka terakhir harus 0 (Contoh 250000)''')

### Fungsi Cek Duplikat ID ###
def cek_duplikat(data, id_mobil):
    for car in data:
        if car['ID'] == id_mobil: # Memeriksa apakah id mobil yang di masukkan terdapat pada data
            return True
    return False

### Fungsi Menambah Mobil ###
def add_car(data):
    add_merk = input_merk() # Memanggil fungsi input merk dan hasil inputan di simpan ke dalam variabel add merk
    add_tipe = input_tipe()
    add_seats = input_seats()
    add_plat = input_plat()
    add_bahan_bakar = input_bahan_bakar()
    add_transmisi = input_transmisi()
    add_status = 'Tersedia' # Untuk mamasukkan nilai otomatis ke dalam status tanpe perlu melakukan inputan
    add_harga = input_harga()
    id_unik = generate_id(add_merk, add_tipe, add_transmisi, data) # Memanggil fungsi validasi id dengan 4 parameter dan di simpan ke variaabel id_mobil
    new_data = {'ID': id_unik, 'merk': add_merk, 'tipe': add_tipe, 'seats': add_seats, 'plat': add_plat, 'bahan_bakar': add_bahan_bakar, 'transmisi': add_transmisi, 'status': add_status, 'harga': add_harga}
    headers = ['ID', 'Merk', 'Tipe', 'Seats', 'Plat_Mobil', 'Bahan_Bakar', 'Transmisi', 'Status', 'Per_Hari_(Rp)']
    print(tabulate([new_data.values()], headers, tablefmt='pretty', stralign='center', numalign='center'))
    confirm = validasi_yes_no()
    if confirm == 'Y':
        data.append(new_data) # Fungsi utama untuk menambahkan data 
        print('Data berhasil ditambahkan')
        return
    elif confirm == 'T':
        print('Penambahan data dibatalkan')
        return

### Fungsi Cek Status Mobil ###
def cek_status(car, new_status):
    if car['status']== new_status: # Mengecek apakah value dari status sama inputan status baru
        return True
    return False

### Fungsi Update Status Mobil ###
def update_status(car):
    while True:
        new_status = input_status()
        if cek_status(car, new_status):
            print('Status baru masih sama dengan status saat ini\nSilahkan pillih status yang berbeda')
            continue
        confirm = validasi_yes_no()
        if confirm == 'Y':
            car['status'] = new_status # Fungsi utama untuk melakukan update pada data
            print('Status mobil berhasil diupdate')
            show_car_list([car]) # Menampilkan data yang telah di update
            return
        elif confirm == 'T':
            print('Update status mobil dibatalkan\n') # jika memasukkan T maka pesan aakaan muncul 
            return
        else:
            print('Pilihan tidak valid') 

### Fungsi Update Harga Mobil ###
def update_harga(car):
    new_harga = input_harga()
    confirm = validasi_yes_no()
    if confirm == 'Y':
        car['harga'] = new_harga # Fungsi utama untuk melakukan update pada dataa
        print('Harga rental berhasil diupdate')
        show_car_list([car]) # Menampilkan data yang telah di update
        return
    elif confirm == 'T':
        print('Update harga rental dibatalkan\n')
        return

### Fungsi Update Mobil ###
def update_car(data, car):
    while True:
        print('''Apa yang ingin Anda update? \n
            1. Status Mobil
            2. Harga Rental Mobil
            3. Kembali ke menu sebelumnya''')
        update = input('\nMasukkan pilihan Anda: ')
        if not update.isdigit() or int(update) not in range(1, 4):
            print('Pilihan tidak valid. Masukkan hanya angka')
            continue
        if update == '1':
            update_status(car) # Jika memilih 1 maka akan masuk ke function update status
            break
        elif update == '2': # Jika memilih 2 maka akan masuk ke function update harga
            update_harga(car)
            break
        elif update == '3': # Jika memilih 3 maka akan kembali ke menu sebelumnya
            break

### Fungsi Menghapus Mobil Berdasarkan ID ###
def delete_car(data, car):
    while True:
        confirm = validasi_yes_no()
        if confirm == 'Y':
            data.remove(car) # Fungsi utama untuk menghapus data
            print('Data berhasil dihapus')
            break
        elif confirm == 'T':
            print('Penghapusan data dibatalkan')
            break
        else:
            print('Inputan anda tidak valid. Silahkan masukkan Y atau T')

### Fungsi Menghapus Semua Data Mobil ###
def delete_all_data(data):
    if len(data) == 0:
        print('Data tidak tersedia')
    else:
        print('Jika anda menghapus seluruh data, maka data tidak dapat di kembalikan')
        confirm = validasi_yes_no() # Memanggil fungsi validasi yes no
        if confirm == 'Y':
            data.clear() # Fungsi utama untuk menghapus seluruh dataa
            print('Seluruh data berhasil dihapus')
        elif confirm == 'T':
            print('Penghapusan seluruh data dibatalkan')

### Fungsi Menu Membaca Data ###
def read_menu(data):
    while True:
        print('''\nSelamat Datang di MOBILPEDIA\n
            1. Menampilkan Seluruh Daftar Mobil
            2. Menampilkan Data Spesifik Berdasarkan ID 
            3. Menampilkan Data Mobil Berdasarkan Transmisi Dan Rentang Harga
            4. Kembali Ke Menu Utama''')
        pilihan = input('\nSilahkan pilih menu yang tersedia : ')
        if not pilihan.isdigit() or int(pilihan) not in range(1, 5): 
            print('Inputan yang anda masukkan tidak tersedia pada pilihan menu')
            continue
        if pilihan == '1':
            show_car_list(data)
        elif pilihan == '2':
            if len(data) == 0:
                print('Data tidak tersedia')
            else:
                car_by_id(data) # Jika terdapat data maka akan di tampilkan
        elif pilihan == '3':
            filter_transmisi_harga(data) # Memanggil fungsi filter
        elif pilihan == '4':
            break

### Fungsi Menu Tambah Mobil ###
def create_menu(data):
    while True:
        print('''\nSelamat Datang di MOBILPEDIA\n
            1. Menambah Data Mobil Rental
            2. Kembali Ke Menu Utama''')
        pilihan = input('\nSilahkan pilih menu yang tersedia : ')
        if not pilihan.isdigit() or int(pilihan) not in range(1, 3):
            print('Inputan yang anda masukkan tidak tersedia pada pilihan menu')
        else:
            if pilihan == '1':
                add_car(data) # Memanggil fungsi add car untuk memasukkan data baru
            elif pilihan == '2':
                break

### Fungsi Menu Update Mobil ###
def update_menu(data):
    while True:
        print('''Selamat Datang Di MOBILPEDIA\n
            1. Mengupdate Data Mobil Rental
            2. Kembali Ke Menu Utama''')
        pilihan = input('Masukkan pilihan Anda: ')
        if not pilihan.isdigit() or int(pilihan) not in range(1, 3):
            print('Pilihan tidak valid. Masukkan hanya angka')
            continue
        if pilihan == '1':
            car = car_by_id(data) # Memanggil fungsi car by id untuk memasukkan id mobil
            if car:
                update_car(data, car) # Memaanggil fungsi update car 
        elif pilihan == '2':
            break

### Fungsi Menu Hapus Mobil ###
def delete_menu(data):
    while True:
        print('''\nSelamat Datang Di MOBILPEDIA\n
            1. Menghapus Data Berdasarkan ID
            2. Menghapus Seluruh Data 
            3. Kembali Ke Menu Utama''')
        pilihan = input('\nSilahkan pilih menu yang tersedia : ')
        if not pilihan.isdigit() or int(pilihan) not in range(1, 4):
            print('Inputan yang anda masukkan tidak tersedia pada pilihan')
            continue
        if pilihan == '1':
            car = car_by_id(data) # Memanggil fungsi car by id untuk memasukkan id mobil
            if car:
                delete_car(data,car) # Memaanggil fungsi delete car untuk menghapus data berdasarkan id
        elif pilihan == '2':
            delete_all_data(data) # Memaanggil fungsi untuk menghapus semua data 
        else:
            break

### Fungsi Menu Utama ###
def main_menu():
    while True:
        print('''\nSelamat Datang Di MOBILPEDIA\n
        1. Menampilkan Daftar Mobil Rental
        2. Menambah Data Mobil Rental
        3. Mengupdate Informasi Mobil Rental
        4. Menghapus Daftar Mobil Rental
        5. Mengakhiri Program''')
        pilihan = input('\nSilahkan pilih menu yang tersedia: ')
        if pilihan.isdigit() and int(pilihan) in range(1, 6):
            if pilihan == '1':
                read_menu(rental_car) # Jika pilih 1 maka akan masuk ke menu read
            elif pilihan == '2':
                create_menu(rental_car) # Jika pilih 2 maka akan masuk ke menu create
            elif pilihan == '3':
                update_menu(rental_car) # Jika pilih 3 maka akan masuk ke menu update
            elif pilihan == '4':
                delete_menu(rental_car) # Jika pilih 4 maka akan masuk ke menu delete
            elif pilihan == '5':
                confirm = validasi_yes_no()
                if confirm == 'Y': # Jika pilih Y maka akan keluar dari program
                    print('\nTerima kasih telah menggunakan MOBILPEDIA\n')
                    return
                elif confirm == 'T':
                    continue
        else:
            print('Inputan yang anda masukkan tidak tersedia pada pilihan menu')

### Memulai Program ###
if __name__ == '__main__':
    main_menu() # Jika di import sebagai modul tidak akan otomatis running
