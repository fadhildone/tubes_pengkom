#microwave
sistem = "off"
skalar_suhu= 0
suhu = ""
waktu_menit = 0
waktu_detik = 0
mode = "normal"
keep_warm = "off"
jam = "\njam : 12.00\n "
nama = "none"
fungsi = "normal"
penghangat = {"Program": "none", "Temperatur":"none"}
def aktifkan_penghangat(penghangat, N):
    if N == 1:
        penghangat["Program"] = "Program Penghangat Sop"
        penghangat["Temperatur"] = "75° Celsius"
        return penghangat
    elif N == 2:
        penghangat["Program"] = "Program Penghangat Rendang"
        penghangat["Temperatur"] =  " 75° Celsius"
        return penghangat
    elif N == 3:
        penghangat["Program"] = "Program Penghangat Pizza"
        penghangat["Temperatur"] = "75° Celsius"
        return penghangat
    elif N == 4:
        penghangat["Program"] = "Program Penghangat Ayam Goreng"
        penghangat["Temperatur"] = "75° Celsius"
        return penghangat
    elif N == 5:
        penghangat["Program"] = "Program Penghangat Spagetthi"
        penghangat["Temperatur"] = "75° Celsius"
        return penghangat
    elif N == 6:
        penghangat["Program"] = "Program Penghangat Minuman Hangat"
        penghangat["Temperatur"] = "75° Celsius"
        return penghangat
def konverter_Fahrenheit_suhu(suhu):
    if suhu == "Celsius" :
        suhu = "Fahrenheit"
        return suhu
    elif suhu == "Kelvin" :
        suhu = "Fahrenheit"
        return suhu
    elif suhu == "Reamor" :
        suhu = "Fahrenheit"
        return suhu

def konverter_Celsius_suhu(suhu):
    if suhu == "Fahrenheit" :
        suhu = "Celsius"
        return suhu
    elif suhu == "Kelvin" :
        suhu = "Celsius"
        return suhu
    elif suhu == "Reamor" :
        suhu = "Celsius"
        return suhu

def konverter_Kelvin_suhu(suhu):
    if suhu == "Fahrenheit" :
        suhu = "Kelvin"
        return suhu
    elif suhu == "Celsius" :
        suhu = "Kelvin"
        return suhu
    elif suhu == "Reamor" :
        suhu = "Kelvin"
        return suhu

def konverter_Reamor_suhu(suhu):
    if suhu == "Fahrenheit" :
        suhu = "Reamor"
        return suhu
    elif suhu == "Celsius" :
        suhu = "Reamor"
        return suhu
    elif suhu == "Kelvin" :
        suhu = "Reamor"
        return suhu

def konverter_Fahrenheit_skalar(suhu, skalar_suhu):
    if suhu == "Celsius" :
        skalar_suhu = ((skalar_suhu * (9/5) + 32))
        return skalar_suhu
    elif suhu == "Kelvin" :
        skalar_suhu = (((9/5)*(skalar_suhu-273)+32))
        return skalar_suhu
    elif suhu == "Reamor" :
        skalar_suhu = ((skalar_suhu * 9 / 4) + 32)
        return skalar_suhu
def konverter_Celsius_skalar(suhu, skalar_suhu):
    if suhu == "Fahrenheit" :
        skalar_suhu = ((skalar_suhu * 5/9) - 32)
        return skalar_suhu
    elif suhu == "Kelvin" :
        skalar_suhu = (skalar_suhu-273)
        return skalar_suhu
    elif suhu == "Reamor" :
        skalar_suhu = (skalar_suhu * 5 / 4)
        return skalar_suhu

def konverter_Kelvin_skalar(suhu, skalar_suhu):
    if suhu == "Fahrenheit" :
        skalar_suhu = (((skalar_suhu-32) * (5/9)) + 273)
        return skalar_suhu
    elif suhu == "Celsius" :
        skalar_suhu = (skalar_suhu+273)
        return skalar_suhu
    elif suhu == "Reamor" :
        skalar_suhu = ((skalar_suhu * 5 / 4) + 273)
        return skalar_suhu
def konverter_Reamor_skalar(suhu, skalar_suhu):
    if suhu == "Fahrenheit" :
        skalar_suhu = ((skalar_suhu-32) * (4/9) )
        return skalar_suhu
    elif suhu == "Celsius" :
        skalar_suhu = (skalar_suhu * 4 / 5)
        return skalar_suhu
    elif suhu == "Kelvin" :
        skalar_suhu = ((skalar_suhu-273) * 4 / 5)
        return skalar_suhu


while True:
    print (jam)
    print ("Nyalakan microwave (Y/N) ? ")
    perintah = input()
    if perintah == "Y":
        sistem = "on"
        print ("Microwave nyala\n")
        break
    elif perintah == "N":
        sistem = "off"
        print ("Microwave mati")
        break
    else:
        print ("Masukkan tidak valid")


while sistem == "on" :
    if keep_warm == "off":
        print (jam)
        print(f"program: {nama}")
        print(f"Temperatur {skalar_suhu} {suhu}")
        print(f"Timer {waktu_menit}:{waktu_detik}")
        print(f"mode : {mode}")
        print (f"fungsi: {fungsi}\n")
        print ("Silahkan pilih menu yang anda inginkan: ")
        print ("1. masukkan temperatur")
        print ("2. Atur timer")
        print ("3. Atur mode")
        print ("4. Reset Program")
        print ("5. Jalankan program")
        print ("6. Matikan")
        menu = int(input("Masukkan menu yang anda inginkan: "))
        if menu == 1:
            fungsi = "normal"
            while True:
                print (jam)
                print ("\nSilahkan pilih satuan yang anda inginnkan: ")
                print ("1. Celsius")
                print ("2. Fahrenheit")
                print ("3. Kelvin")
                print ("4. Reamor")
                print ("5. Back")
                perintah_1 = int(input("\nSilahkan masukkan pilihan anda: "))
                if perintah_1 == 1:
                    print("Suhu yang anda pilih adalah Celsius")
                    suhu = "Celsius"
                    skalar_suhu = float(input("Silahkan masukkan suhu anda: "))
                    print(f"Anda telah memilih temperatur sebesar {skalar_suhu} derajat celsius\n")
                    break
                elif perintah_1 == 2:
                    print("Suhu yang anda pilih adalah Fahrenheit")
                    suhu = ("Fahrenheit")
                    skalar_suhu = float(input("Silahkan masukkan suhu anda: "))
                    print(f"Anda telah memilih temperatur sebesar {skalar_suhu} derajat fahrenheit\n")
                    break
                elif perintah_1 == 3:
                    print("Suhu yang anda pilih adalah Kelvin")
                    suhu = ("Kelvin")
                    skalar_suhu = float(input("Silahkan masukkan suhu anda: "))
                    print(f"Anda telah memilih temperatur sebesar {skalar_suhu} derajat Kelvin\n")
                    break
                elif perintah_1 == 4:
                    print("Suhu yang anda pilih adalah Reamor")
                    suhu = "Reamor"
                    skalar_suhu = float(input("Silahkan masukkan temperatur anda: "))
                    print(f"Anda telah memilih temperatur sebesar {skalar_suhu} derajat Reamor\n")
                    break
                elif perintah_1 == 5:
                    break
                else:
                    print ("Masukkan tidak valid")

            while suhu == "Celsius" or suhu == "Kelvin" or suhu == "Reamor" or suhu == "Fahrenheit":
                 print (jam)
                 print ("Apakah anda ingin mengganti besaran temperatur (Y/N)?\n")
                 perintah_2 = input()
                 if perintah_2 == "N":
                     print (f"temperatur tetap dalam {suhu}")
                     break
                 elif perintah_2 == "Y":
                     print (jam)
                     while suhu == "Celsius":
                         print ("Silahkan pilih tujuan temperatur")
                         print ("1. Fahrenheit")
                         print ("2. Kelvin")
                         print ("3. Reamor")
                         print ("4. Kembali")
                         print ("Silahkan masukkan tujuan temperatur")
                         ubah = int(input())
                         if ubah == 1:
                             skalar_suhu = konverter_Fahrenheit_skalar(suhu,skalar_suhu)
                             suhu = konverter_Fahrenheit_suhu(suhu)
                             print (f"\ntemperatur telah diubah ke dalam {suhu}")
                             break
                         elif ubah == 2:
                             skalar_suhu = konverter_Kelvin_skalar(suhu,skalar_suhu)
                             suhu = konverter_Kelvin_suhu(suhu)
                             print (f"\ntemperatur telah diubah ke dalam {suhu}")
                             break
                         elif ubah == 3:
                             skalar_suhu = konverter_Reamor_skalar(suhu,skalar_suhu)
                             suhu = konverter_Reamor_suhu(suhu)
                             print(f"\ntemperatur telah diubah ke dalam {suhu}")
                             break
                         elif ubah == 4:
                             print ("temperatur tidak diubah")
                             break
                     while suhu == "Fahrenheit":
                         print (jam)
                         print ("Silahkan pilih tujuan temperatur")
                         print ("1. Celsius")
                         print ("2. Kelvin")
                         print ("3. Reamor")
                         print ("4. Kembali")
                         print ("Silahkan masukkan tujuan temperatur")
                         ubah = int(input())
                         if ubah == 1:
                             skalar_suhu = konverter_Celsius_skalar(suhu,skalar_suhu)
                             suhu = konverter_Celsius_suhu(suhu)
                             print (f"\ntemperatur telah diubah ke dalam {suhu}")
                             break
                         elif ubah == 2:
                             skalar_suhu = konverter_Kelvin_skalar(suhu,skalar_suhu)
                             suhu = konverter_Kelvin_suhu(suhu)
                             print (f"\ntemperatur telah diubah ke dalam {suhu}")
                             break
                         elif ubah == 3:
                             skalar_suhu = konverter_Reamor_skalar(suhu,skalar_suhu)
                             suhu = konverter_Reamor_suhu(suhu)
                             print(f"\ntemperatur telah diubah ke dalam {suhu}")
                             break
                         elif ubah == 4:
                             print ("temperatur tidak diubah")
                             break
                     while suhu == "Reamor":
                         print (jam)
                         print ("Silahkan pilih tujuan temperatur")
                         print ("1. Celsius")
                         print ("2. Kelvin")
                         print ("3. Fahrenheit")
                         print ("4. Kembali")
                         print ("Silahkan masukkan tujuan temperatur")
                         ubah = int(input())
                         if ubah == 1:
                             skalar_suhu = konverter_Celsius_skalar(suhu,skalar_suhu)
                             suhu = konverter_Celsius_suhu(suhu)
                             print (f"\ntemperatur telah diubah ke dalam {suhu}")
                             break
                         elif ubah == 2:
                             skalar_suhu = konverter_Kelvin_skalar(suhu,skalar_suhu)
                             suhu = konverter_Kelvin_suhu(suhu)
                             print (f"\ntemperatur telah diubah ke dalam {suhu}")
                             break
                         elif ubah == 3:
                             skalar_suhu = konverter_Fahrenheit_skalar(suhu,skalar_suhu)
                             suhu = konverter_Fahrenheit_suhu(suhu)
                             print(f"\ntemperatur telah diubah ke dalam {suhu}")
                             break
                         elif ubah == 4:
                             print ("temperatur tidak diubah")
                             break
                         else:
                             print ("Masukkan tidak valid")
                     while suhu == "Kelvin":
                         print (jam)
                         print ("Silahkan pilih tujuan temperatur")
                         print ("1. Celsius")
                         print ("2. Reamor")
                         print ("3. Fahrenheit")
                         print ("4. Kembali")
                         print ("Silahkan masukkan tujuan temperatur")
                         ubah = int(input())
                         if ubah == 1:
                             skalar_suhu = konverter_Celsius_skalar(suhu,skalar_suhu)
                             suhu = konverter_Celsius_suhu(suhu)
                             print (f"\ntemperatur telah diubah ke dalam {suhu}")
                             break
                         elif ubah == 2:
                             skalar_suhu = konverter_Reamor_skalar(suhu,skalar_suhu)
                             suhu = konverter_Reamor_suhu(suhu)
                             print (f"\ntemperatur telah diubah ke dalam {suhu}")
                             break
                         elif ubah == 3:
                             skalar_suhu = konverter_Fahrenheit_skalar(suhu,skalar_suhu)
                             suhu = konverter_Fahrenheit_suhu(suhu)
                             print(f"\ntemperatur telah diubah ke dalam {suhu}")
                             break
                         elif ubah == 4:
                             print ("temperatur tidak diubah")
                             break
                         else:
                             print("Masukkan tidak valid")
                     break
                 else:
                     print ("Masukkan tidak valid")

        elif menu == 2:
            fungsi = "normal"
            while True:
                print (jam)
                print ("Pilih timer yang ada:  ")
                print ("1. 1 menit")
                print ("2. 3 menit")
                print ("3. 5 menit")
                print ("4. 10 menit")
                print ("5. 15 menit")
                print ("6. 20 menit")
                print ("7. 30 menit")
                print ("8. Masukkan secara manual")
                print ("9. Kembali")
                print ("Pilih opsi timer yang ada:")
                perintah_3 = int(input())
                if perintah_3 == 1:
                    waktu_menit = 1
                    print (f"timer anda adalah {waktu_menit} menit {waktu_detik} detik")
                    break
                elif perintah_3 == 2:
                    waktu_menit = 3
                    print(f"timer anda adalah {waktu_menit} menit {waktu_detik} detik")
                    break
                elif perintah_3 == 3:
                    waktu_menit = 5
                    print(f"timer anda adalah {waktu_menit} menit {waktu_detik} detik")
                    break
                elif perintah_3 == 4:
                    waktu_menit = 10
                    print(f"timer anda adalah {waktu_menit} menit {waktu_detik} detik")
                    break
                elif perintah_3 == 5:
                    waktu_menit = 15
                    print(f"timer anda adalah {waktu_menit} menit {waktu_detik} detik")
                    break
                elif perintah_3 == 6:
                    waktu_menit = 20
                    print(f"timer anda adalah {waktu_menit} menit {waktu_detik} detik")
                    break
                elif perintah_3 == 7:
                    waktu_menit = 30
                    print(f"timer anda adalah {waktu_menit} menit {waktu_detik} detik")
                    break
                elif perintah_3 == 8:
                    waktu_menit = int(input("Masukkan menit: "))
                    waktu_detik = int(input("Masukkan detik: "))
                    print(f"timer anda adalah {waktu_menit} menit {waktu_detik} detik")
                    break
                elif perintah_3 == 9:
                    break
                else:
                    print ("Masukkan tidak valid")




        elif menu == 3:
            while sistem == "on":
                print (jam)
                print ("Silahkan pilih mode yang anda inginkan")
                print ("1. Eco Mode")
                print ("2. Clean by Steaming")
                print ("3. Keep Warm")
                print ("4. Kembali")
                print ("Silahkan masukkan pilihan anda: ")
                perintah_4 = int(input())
                if perintah_4 == 1:
                    print ("\njam digital dimatikan\n")
                    mode = "Eco Mode"
                    jam = ""
                    break
                elif perintah_4 == 2:
                    skalar_suhu = 0
                    suhu = ""
                    waktu_menit = 5
                    waktu_detik = 0
                    fungsi = "Clean by Steaming"
                    nama = "none"
                    keep_warm = "off"
                    print("Fungsi microwave diubah menjadi Clean by Steaming\nMembersihkan makanan dengan metode steaming")
                    break
                elif perintah_4 == 3:
                    print (jam)
                    waktu_detik = 0
                    waktu_menit = 0
                    print ("Silahkan pilih menu makanan")
                    print ("1. Sop")
                    print ("2. Rendang")
                    print ("3. Pizza")
                    print ("4. Ayam Goreng")
                    print ("5. Spagetthi")
                    print ("6. Minuman Hangat")
                    print ("7. Kembali")
                    print ("Silahkan masukkan pilihan anda: ")
                    N = int(input())
                    if N == 1:
                        print(jam)
                        aktifkan_penghangat(penghangat,1)
                        print ("program penghangat Sop")
                        waktu_menit = int(input("Masukkan lama waktu (menit): "))
                        waktu_detik = int(input("Masukkan lama waktu (detik): "))
                        keep_warm = "on"
                        break
                    elif N == 2:
                        print(jam)
                        aktifkan_penghangat(penghangat,2)
                        print ("program penghangat Rendang")
                        waktu_menit = int(input("Masukkan lama waktu (menit): "))
                        waktu_detik = int(input("Masukkan lama waktu (detik): "))
                        keep_warm = "on"
                        break
                    elif N == 3:
                        print(jam)
                        aktifkan_penghangat(penghangat,3)
                        print ("program penghangat Pizza")
                        waktu_menit = int(input("Masukkan lama waktu (menit): "))
                        waktu_detik = int(input("Masukkan lama waktu (detik): "))
                        keep_warm = "on"
                        break
                    elif N == 4:
                        print(jam)
                        aktifkan_penghangat(penghangat,4)
                        print ("program penghangat Ayam Goreng")
                        waktu_menit = int(input("Masukkan lama waktu (menit): "))
                        waktu_detik = int(input("Masukkan lama waktu (detik): "))
                        keep_warm = "on"
                        break
                    elif N == 5:
                        print(jam)
                        aktifkan_penghangat(penghangat,5)
                        print ("program penghangat Spagetthi")
                        waktu_menit = int(input("Masukkan lama waktu (menit): "))
                        waktu_detik = int(input("Masukkan lama waktu (detik): "))
                        keep_warm = "on"
                        break
                    elif N == 6:
                        print(jam)
                        aktifkan_penghangat(penghangat,6)
                        print ("program penghangat Minuman Hangat")
                        waktu_menit = int(input("Masukkan lama waktu (menit): "))
                        waktu_detik = int(input("Masukkan lama waktu (detik): "))
                        keep_warm = "on"
                        break
                    elif N == 7:
                        break
                    else:
                        print(jam)
                        print("Masukkan tidak valid")
                elif perintah_4 == 4:
                    break
                else:
                    print ("Masukkan tidak valid")


        elif menu == 4:
            skalar_suhu = 0
            suhu = ""
            waktu_menit = 0
            waktu_detik = 0
            mode = "normal"
            fungsi = "normal"
            jam = "\njam : 12.00\n "
            nama = "none"
            keep_warm = "off"
            print ("Semua Program telah direset")

        elif menu == 5:
            print (jam)
            print ("Program dijalankan")
            print (f"nama Program: {nama}")
            print (f"Temperatur sebesar: {skalar_suhu} {suhu}")
            print (f"Timer {waktu_menit}:{waktu_detik}")
            print (f"mode : {mode}")
            print (f"fungsi : {fungsi}")
            break
        elif menu == 6:
            print ("\nmicrowave dimatikan")
            break
        else:
            print("\nmasukkan tidak valid")
    elif keep_warm == "on":
        fungsi = "keep warm"
        print(jam)
        for key, value in penghangat.items():
            print(f"{key} : {value}")
        print(f"Timer {waktu_menit}:{waktu_detik}")
        print(f"mode : {mode}")
        print(f"fungsi: {fungsi}\n")
        print("Silahkan pilih menu yang anda inginkan: ")
        print("1. Atur mode")
        print("2. Reset Program")
        print("3. Jalankan program")
        print("4. Matikan")
        menu = int(input("Masukkan menu yang anda inginkan: "))
        if menu == 1:
            while sistem == "on":
                print(jam)
                print("Silahkan pilih mode yang anda inginkan")
                print("1. Eco Mode")
                print("2. Clean by Steaming")
                print("3. Keep Warm")
                print("4. Kembali")
                print("Silahkan masukkan pilihan anda: ")
                perintah_4 = int(input())
                if perintah_4 == 1:
                    print("\njam digital dimatikan\n")
                    mode = "Eco Mode"
                    jam = ""
                    break
                elif perintah_4 == 2:
                    skalar_suhu = 0
                    suhu = ""
                    waktu_menit = 5
                    waktu_detik = 0
                    fungsi = "Clean by Steaming"
                    jam = "\njam : 12.00\n "
                    nama = "none"
                    keep_warm = "off"
                    print("Fungsi microwave diubah menjadi Clean by Steaming\nMembersihkan makanan dengan metode steaming")
                    break
                elif perintah_4 == 3:
                    print(jam)
                    waktu_detik = 0
                    waktu_menit = 0
                    print("Silahkan pilih menu makanan")
                    print("1. Sop")
                    print("2. Rendang")
                    print("3. Pizza")
                    print("4. Ayam Goreng")
                    print("5. Spagetthi")
                    print("6. Minuman Hangat")
                    print("Silahkan masukkan pilihan anda: ")
                    N = int(input())
                    if N == 1:
                        print(jam)
                        aktifkan_penghangat(penghangat, 1)
                        print("program penghangat Sop")
                        waktu_menit = int(input("Masukkan lama waktu (menit): "))
                        waktu_detik = int(input("Masukkan lama waktu (detik): "))
                        keep_warm = "on"
                        break
                    elif N == 2:
                        print(jam)
                        aktifkan_penghangat(penghangat, 2)
                        print("program penghangat Rendang")
                        waktu_menit = int(input("Masukkan lama waktu (menit): "))
                        waktu_detik = int(input("Masukkan lama waktu (detik): "))
                        keep_warm = "on"
                        break
                    elif N == 3:
                        print(jam)
                        aktifkan_penghangat(penghangat, 3)
                        print("program penghangat Pizza")
                        waktu_menit = int(input("Masukkan lama waktu (menit): "))
                        waktu_detik = int(input("Masukkan lama waktu (detik): "))
                        keep_warm = "on"
                        break
                    elif N == 4:
                        print(jam)
                        aktifkan_penghangat(penghangat, 4)
                        print("program penghangat Ayam Goreng")
                        waktu_menit = int(input("Masukkan lama waktu (menit): "))
                        waktu_detik = int(input("Masukkan lama waktu (detik): "))
                        keep_warm = "on"
                        break
                    elif N == 5:
                        print(jam)
                        aktifkan_penghangat(penghangat, 5)
                        print("program penghangat Spagetthi")
                        waktu_menit = int(input("Masukkan lama waktu (menit): "))
                        waktu_detik = int(input("Masukkan lama waktu (detik): "))
                        keep_warm = "on"
                        break
                    elif N == 6:
                        print(jam)
                        aktifkan_penghangat(penghangat, 6)
                        print("program penghangat Minuman Hangat")
                        waktu_menit = int(input("Masukkan lama waktu (menit): "))
                        waktu_detik = int(input("Masukkan lama waktu (detik): "))
                        keep_warm = "on"
                        break
                    elif N == 7:
                        break
                    else:
                        print(jam)
                        print("Masukkan tidak valid")

                else:
                    print("Masukkan tidak valid")


        elif menu == 2:
            skalar_suhu = 0
            suhu = ""
            waktu_menit = 0
            waktu_detik = 0
            mode = "normal"
            fungsi = "normal"
            jam = "\njam : 12.00\n "
            nama = "none"
            keep_warm = "off"
            print("Semua Program telah direset")

        elif menu == 3:
            print(jam)
            print("Program dijalankan")
            for key, value in penghangat.items():
                print(f"{key} : {value}")
            print(f"Timer {waktu_menit}:{waktu_detik}")
            print(f"mode: {mode}")
            print (f"fungsi : {fungsi}")
            break
        elif menu == 4:
            print("\nmicrowave dimatikan")
            break
        else:
            print("\nmasukkan tidak valid")

