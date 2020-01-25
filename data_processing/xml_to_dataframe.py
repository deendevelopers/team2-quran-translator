import numpy as np
import pandas as pd
from pathlib import Path
import xml.etree.ElementTree as ET

xml_quran_fp = Path('../data/quran-uthmani.xml')
xml_quran_root = ET.parse(xml_quran_fp).getroot()
columns = ['Surah Name', 'Surah Number', 'Verse Number', 'Verse Text']
df = pd.DataFrame(columns=columns)

xml_trans_files = list(Path('../data/en_trans_xml_files').iterdir())

def gather_translations_df():
    for xml_en_file in xml_trans_files:
        trans_code = xml_en_file.name.strip('.xml').replace('.', '_')
        print(trans_code)
        df[trans_code] = np.nan
        root = ET.parse(xml_en_file).getroot()
        for sura_element in root:
            sura_num = int(sura_element.attrib.get('index'))
            sura_name = sura_element.attrib.get('name')
            for verse_element in sura_element:
                verse_num = int(verse_element.get('index'))
                verse_text = verse_element.get('text')
                df[trans_code].loc[sura_num, verse_num] = verse_text
    return df