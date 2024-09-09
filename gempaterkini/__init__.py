from bs4 import BeautifulSoup
import requests

def extraction_data():
    """
    hasil = dict()
    hasil['tanggal']    = '07 September 2024'
    hasil['waktu']      = '20:51:13 WIB'
    hasil['magnitudo']  = 3.6
    hasil['lokasi']     = {'ls':4.12, 'bt':129.79}
    hasil['pusat gempa']= 'Pusat gempa berada di laut 47 km Utara Banda'
    hasil['dirasakan']  = 'Dirasakan (Skala MMI): II-III Banda'

    return hasil
    """

    try:
        content = requests.get('https://www.bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        calendar = soup.find('span', {'class': 'waktu'})
        calendar = calendar.text.split(', ')
        waktu    = calendar[1]
        tanggal  = calendar[0]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = soup.findChildren('li')
        i = 0

        magnitudo   = None
        ls          = None
        bt          = None
        kedalaman   = None
        dirasakan   = None
        lokasi      = None

        for res in result:
            # print (i, res)
            if i == 140:
                magnitudo = res.text
            elif i == 141:
                kedalaman = res.text
            elif i == 142:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 143:
                lokasi = res.text
            elif i == 144:
                dirasakan = res.text

            i = i+1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['pusat'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil

        # print(content.text, 'html.parser')

    else:
        return None

    # soup = BeautifulSoup(content)
    # print (soup.prettify())

def show_data(result):
    if result is None:
        print("Tidak dapat menemukan data gempa terkini")
        return

    print('Gempa terakhir berdasarkan data dari BMKG')
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Koordinat : {result['koordinat']['ls']}, {result['koordinat']['bt']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Pusat Gempa : {result['pusat']}")
    print(f"Dirasakan : {result['dirasakan']}")

    #print('Tanggal', result['tanggal'])