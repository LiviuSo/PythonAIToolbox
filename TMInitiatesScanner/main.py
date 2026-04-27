from TMInitiatesScanner.DataPipeline import pipeline
from pathlib import Path

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    base_dir = Path(__file__).resolve().parent.parent

    # filepath = base_dir / "TMInitiatesScanner" / "data" / "images" # extract from images
    filepath = base_dir / "TMInitiatesScanner" / "data" / "pdf"  # extract from a pdf having an instruction per page
    # filepath = base_dir / "TMInitiatesScanner" / "data" / "pdfs" # extract from multiple pdfs, each having an instruction on one page
    excel_path = base_dir / "TMInitiatesScanner" / "data" / "output" / "Adela_ baza de date Meditatori.xlsx"  # save to this Excel file
    start_row= 140

    pipeline(str(filepath), str(excel_path), start_row)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
