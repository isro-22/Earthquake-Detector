# ...............................
# Application Earthquake-Detector
# Modularisasi dengan Python
# ...............................
# from gempaterkini import extraction_data, show_data
import gempaterkini

if __name__ == '__main__':
    print('Applikasi Utama')

    result = gempaterkini.extraction_data()
    gempaterkini.show_data(result)