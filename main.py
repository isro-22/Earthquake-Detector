# ...............................
# Application Earthquake-Detector
# Modularisasi dengan Python
# ...............................

def extraction_data():
    hasil = dict()
    hasil['tanggal']    = '24 Agustus 2024'
    hasil['waktu']      = '12:05:52 WIB'
    hasil['magnitudo']  = 4.0
    hasil['lokasi']     = {'ls':1.48, 'bt':134.01}
    hasil['pusat gempa']= 'Pusat gempa berada di laut 47 km Utara Banda'
    hasil['dirasakan']  = 'Dirasakan (Skala MMI): II-III Banda'

    return hasil

def show_data(result):
    print('Gempa terakhir berdasarkan data dari BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi : LS {result['lokasi']['ls']}, BT {result['lokasi']['bt']}")
    print(f"Pusat Gempa {result['pusat gempa']}")
    print(f"Dirasakan {result['dirasakan']}")

    #print('Tanggal', result['tanggal'])


if __name__ == '__main__':
    print('Applikasi Utama')

    result = extraction_data()
    show_data(result)