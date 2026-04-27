import pandas as pd

INDEX_PRENUME = 1
INDEX_PRENUME_ADITIONAL = 2
INDEX_NUME = 3
INDEX_DATA_NASTERII = 5
INDEX_VARSTA = 6
INDEX_TELEFON = 9
INDEX_EMAIL = 10
INDEX_ADRESA_EMAIL_ELIMINATA = 11
INDEX_LOCALITATE_REZIDENTA = 12
INDEX_CENTRU_MT = 13
INDEX_LOCALITATE_INSTRUIRE = 14
INDEX_DATA_INSTRUIRE = 15
INDEX_INSTRUCTOR = 16
INDEX_MOTIV_INSTRUIRE = 17
INDEX_CUM_AUZIT_DE_MT = 18
INDEX_PROFESIE = 19

VALUE_PLACEHOLDER = "-"
VALUE_CENTRU = "Bucureşti"
VALUE_LOCALITATE = "Bucureşti"
VALUE_INSTRUCTOR = "Adela Herea"

# 0: 'Unnamed: 0'
# 1: 'Prenume \n(fara diacritice)'
# 2: 'Prenume Aditional \n(fara diacritice)'
# 3: 'Nume \n(fara diacritice)'
# 4: 'Status Membru Asociatie'
# 5: 'Data nasterii'
# 6: 'Vârsta'
# 7: 'Status'
# 8: 'Curs fizic / TM app'
# 9: 'Date contact tel'
# 10: 'Adresa email principala'
# 11: 'Adresa email eliminata'
# 12: 'Localitate de rezidenta'
# 13: 'Centru MT'
# 14: 'Instruire MT - Localitate'
# 15: 'Instruire MT – data'
# 16: 'Instructor MT'
# 17: 'Motiv instruire '
# 18: 'Cum ați auzit de MT?'
# 19: 'Profesie'
# 20: 'Taxa curs (EUR)'
# 21: 'Taxa curs (EUR).1'
# 22: 'Taxa Curs (RON)'
# 23: 'Suma aferenta Instructorului (RON) 70%'
# 24: 'Categoria reducerii aplicate(daca este cazul)'
# 25: 'Categorie membru'
# 26: 'Google group'
# 27: 'Whatsapp group'
# 28: 'T1 – Localitate'
# 29: 'T1 - Data'
# 30: 'T1 - Intructor'
# 31: 'T2 – Localitate'
# 32: 'T2 - Data'
# 33: 'T2 - Instructor'
# 34: 'T3 – Localitate'
# 35: 'T3- Data'
# 36: 'T3 - Instructor'
# 37: 'T4 - Localitate'
# 38: 'T4 - Data'
# 39: 'T4 - Instructor'
# 40: 'Sidhi – Localitate Curs'
# 41: 'Sidhi - Data curs'
# 42: 'Sidhi - Instructor Curs'
# 43: 'Sidhi – Localitate Flying'
# 44: 'Sidhi - Data Flying'
# 45: 'Sidhi - Instructor Flying'
# 46: 'TTC – Locatie'
# 47: 'TTC - Perioada'
# 48: 'Status Instructor'
# 49: 'Decedat an'

columns = [
    'Undefined: 0',  # 0
    'Prenume \n(fara diacritice)',  # 1
    'Prenume Aditional \n(fara diacritice)',  # 2
    'Nume \n(fara diacritice)',  # 3
    'Status Membru Asociatie',  # 4
    'Data nasterii',  # 5
    'Vârsta',  # 6
    'Status',  # 7
    'Curs fizic / TM app',  # 8
    'Date contact tel',  # 9
    'Adresa email principala',  # 10
    'Adresa email eliminata',
    'Localitate de rezidenta',
    'Centru MT',
    'Instruire MT - Localitate',
    'Instruire MT – data',
    'Instructor MT',
    'Motiv instruire ',
    'Cum ați auzit de MT?',
    'Profesie',
    'Taxa curs (EUR)',
    'Taxa curs (EUR).1',
    'Taxa Curs (RON)',
    'Suma aferenta Instructorului (RON) 70%',
    'Categoria reducerii aplicate(daca este cazul)',
    'Categorie membru',
    'Google group',
    'Whatsapp group',
    'T1 – Localitate',
    'T1 - Data',
    'T1 - Intructor',
    'T2 – Localitate',
    'T2 - Data',
    'T2 - Instructor',
    'T3 – Localitate',
    'T3- Data',
    'T3 - Instructor',
    'T4 - Localitate',
    'T4 - Data',
    'T4 - Instructor',
    'Sidhi – Localitate Curs',
    'Sidhi - Data curs',
    'Sidhi - Instructor Curs',
    'Sidhi – Localitate Flying',
    'Sidhi - Data Flying',
    'Sidhi - Instructor Flying',
    'TTC – Locatie',
    'TTC - Perioada',
    'Status Instructor',
    'Decedat an'
]
# {'principale motive pentru care doriti sǎ invǎtati MT': '— (necompletat)', 'cum ati auzit de Meditatia Transcedentalǎ': 'David Lynch (pe YouTube)'}
RAW_KEY_DATA_INSTRUIRE = 'data instruire'
RAW_KEY_NUME = 'nume de familie'
RAW_KEY_PRENUME = 'prenume'
RAW_KEY_PRENUME_ADITIONAL = 'prenume aditional'
RAW_KEY_VARSTA = 'varsta'
RAW_KEY_DATA_DATA_NASTERII = 'data nasterii'
RAW_KEY_ORAS_REZINDENTA = 'orasul din adresa'
RAW_KEY_TELEFON = 'telefon'
RAW_KEY_EMAIL = 'email'
RAW_KEY_PROFESIE = 'profesie'
RAW_KEY_MOTIV_INSTRUIRE = 'principalele motive pentru care doriti sa invatati mt'
RAW_KEY_CUM_AUZIT_DE_MT = 'cum ati auzit de meditatia transcedentala'


def remove_diacritics(text: str) -> str:
    """Remove Romanian diacritics from a string."""
    diacritics = {
        'ă': 'a', 'â': 'a', 'î': 'i', 'ș': 's', 'ț': 't',
        'Ă': 'A', 'Â': 'A', 'Î': 'I', 'Ș': 'S', 'Ț': 'T',
        'ǎ': 'a', 'Ǎ': 'A',  # ← Add these (a-caron)
    }
    for diacritic, replacement in diacritics.items():
        text = text.replace(diacritic, replacement)
    return text


def create_dict_from_data(data: str) -> dict[str, str]:
    result = {}
    for line in data.split("\n"):
        if ":" in line:
            parts = line.split(":", 1)  # Split only on FIRST colon
            key = parts[0].strip("- **")
            value = parts[1].strip(" **") if len(parts) > 1 else ""
            result[remove_diacritics(key).lower()] = value
    return result


def clean_data(read_data: dict[str, str]) -> dict[str, str]:
    tm_data = {}

    for col in columns:
        tm_data[col] = ""

    tm_data[columns[INDEX_PRENUME]] = read_data.get(RAW_KEY_PRENUME, "")
    tm_data[columns[INDEX_PRENUME_ADITIONAL]] = read_data.get(RAW_KEY_PRENUME_ADITIONAL, VALUE_PLACEHOLDER)
    tm_data[columns[INDEX_NUME]] = read_data.get(RAW_KEY_NUME, "")
    tm_data[columns[INDEX_DATA_NASTERII]] = convert_date_ro(read_data.get(RAW_KEY_DATA_DATA_NASTERII, ""))
    tm_data[columns[INDEX_VARSTA]] = read_data.get(RAW_KEY_VARSTA, "")
    tm_data[columns[INDEX_TELEFON]] = read_data.get(RAW_KEY_TELEFON, "")
    tm_data[columns[INDEX_EMAIL]] = read_data.get(RAW_KEY_EMAIL, "")
    tm_data[columns[INDEX_ADRESA_EMAIL_ELIMINATA]] = VALUE_PLACEHOLDER
    tm_data[columns[INDEX_LOCALITATE_REZIDENTA]] = read_data.get(RAW_KEY_ORAS_REZINDENTA, "")
    tm_data[columns[INDEX_CENTRU_MT]] = VALUE_CENTRU
    tm_data[columns[INDEX_LOCALITATE_INSTRUIRE]] = VALUE_LOCALITATE
    tm_data[columns[INDEX_DATA_INSTRUIRE]] = convert_date_ro(read_data.get(RAW_KEY_DATA_INSTRUIRE, ""))
    tm_data[columns[INDEX_INSTRUCTOR]] = VALUE_INSTRUCTOR
    tm_data[columns[INDEX_MOTIV_INSTRUIRE]] = read_data.get(RAW_KEY_MOTIV_INSTRUIRE, "")
    tm_data[columns[INDEX_CUM_AUZIT_DE_MT]] = read_data.get(RAW_KEY_CUM_AUZIT_DE_MT, "")
    tm_data[columns[INDEX_PROFESIE]] = read_data.get(RAW_KEY_PROFESIE, "")

    return tm_data


def save_to_excel(output_path: str, list_of_dicts: list[dict[str, str]], start_row: int = 106):
    """
    save the dataframe to xlsx at line 110 keeping the old content
    :param output_path:
    :param list_of_dicts:
    :param start_row:
    :return:
    """
    with pd.ExcelWriter(
            path=output_path,
            engine="openpyxl",
            mode="a",
            if_sheet_exists="overlay"  # ← Add this
    ) as writer:
        df = pd.DataFrame(list_of_dicts)
        df.to_excel(writer, startrow=start_row - 1, index=False, header=False)


def convert_date_ro(date_str: str) -> str:
    """Convertește data din format DD.MM.YYYY în DD-lun.-YYYY

    Exemple:
        03.01.1983 -> 03-ian.-1983
        02.12.1973 -> 02-dec.-1973
    """
    months = {
        1: 'ian.', 2: 'feb.', 3: 'mar.', 4: 'apr.',
        5: 'mai.', 6: 'iun.', 7: 'iul.', 8: 'aug.',
        9: 'sep.', 10: 'oct.', 11: 'nov.', 12: 'dec.'
    }

    parts = date_str.split('.')
    if len(parts) != 3:
        return date_str  # Return as-is if format is unexpected or empty
    day = parts[0]
    month = int(parts[1])
    year = parts[2]

    return f"{day}-{months[month]}-{year}"
