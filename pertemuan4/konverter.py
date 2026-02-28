# konverter.py
'''
berisi fungsi untuk mengonversi mata uang antara Rupiah (IDR)
 dan mata uang lain berdasarkan kurs yang ada di kurs.py
 '''

import kurs

## dari kusr lain ke idr
def USD_ke_IDR(jumlah_Awal) :
    jumlah_Akhir = jumlah_Awal * kurs.kurs['USD']
    return jumlah_Akhir

def EUR_ke_IDR(jumlah_Awal) :
    jumlah_Akhir = jumlah_Awal * kurs.kurs['EUR']
    return jumlah_Akhir


def SGD_ke_IDR(jumlah_Awal) :
    jumlah_Akhir = jumlah_Awal * kurs.kurs['SGD']
    return jumlah_Akhir

def JPY_ke_IDR(jumlah_Awal) :
    jumlah_Akhir = jumlah_Awal * kurs.kurs['JPY']
    return jumlah_Akhir 
## dari idr ke kurs lain
def IDR_ke_USD(jumlah_Awal) :
    jumlah_Akhir = jumlah_Awal / kurs.kurs['USD']
    return jumlah_Akhir

def IDR_ke_EUR(jumlah_Awal) :
    jumlah_Akhir = jumlah_Awal / kurs.kurs['EUR']
    return jumlah_Akhir


def IDR_ke_SGD(jumlah_Awal) :
    jumlah_Akhir = jumlah_Awal / kurs.kurs['SGD']
    return jumlah_Akhir

def IDR_ke_JPY(jumlah_Awal) :
    jumlah_Akhir = jumlah_Awal / kurs.kurs['JPY']
    return jumlah_Akhir



