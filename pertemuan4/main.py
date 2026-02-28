# main.py

import tabulate
import kurs
import konverter

print("=== KONVERTER MATA UANG ===")


# untuk menampilkan tabel kurs

data = []
for k, v in kurs.kurs.items():
    data.append([k, f"{v:,.0f}".replace(",", ".")])

print(tabulate.tabulate(data, headers=["Kode", "Kurs"], tablefmt="pretty"))

# Input dari user

dari = input("\nDari (IDR/USD/EUR/SGD/JPY): ").upper()
ke = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
jumlah = float(input("Jumlah: "))


#ubah dari kurs asing ke IDR

if dari.upper() == 'USD' :
    jumlahIDR = konverter.USD_ke_IDR(jumlah)
elif dari.upper() == 'EUR' :
    jumlahIDR = konverter.EUR_ke_IDR(jumlah)
elif dari.upper() == 'SGD' :
    jumlahIDR = konverter.SGD_ke_IDR(jumlah)
elif dari.upper() == 'JPY' :
    jumlahIDR = konverter.JPY_ke_IDR(jumlah)
elif dari.upper() == 'IDR' :
    jumlahIDR = jumlah
else :
    print('mata uang tidak valid!')
    jumlahIDR = None



# udah dari idr ke kurs asing

if ke.upper() == 'USD' :
    jumlahKonversi = konverter.IDR_ke_USD(jumlahIDR)
elif ke.upper() == 'EUR' :
    jumlahKonversi = konverter.IDR_ke_EUR(jumlahIDR)
elif ke.upper() == 'SGD' :
    jumlahKonversi= konverter.IDR_ke_SGD(jumlahIDR)
elif ke.upper() == 'JPY' :
    jumlahKonversi= konverter.IDR_ke_JPY(jumlahIDR)
elif ke.upper() == 'IDR' :
    jumlahKonversi = jumlahIDR
else :
    print('mata uang tidak valid')
    jumlahKonversi = None


#output hasil

if jumlahIDR is not None and jumlahKonversi is not None:

    if dari == "IDR":
        print(f"\nRp {jumlah:,.0f}".replace(",", ".") +
              f" = {jumlahKonversi:.2f} {ke}")

    elif ke == "IDR":
        print(f"\n{jumlah:.2f} {dari} = Rp {jumlahKonversi:,.0f}".replace(",", "."))

    else:
        print(f"\n{jumlah:.2f} {dari} = {jumlahKonversi:.2f} {ke}")