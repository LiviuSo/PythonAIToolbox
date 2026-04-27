# Pipeline for extracting data from images
import os

from TMInitiatesScanner.DataExtractorGPT import init_openai
from TMInitiatesScanner.DataExtractorGPT import extract_data_from_image
from TMInitiatesScanner.DataWriter import create_dict_from_data, clean_data, save_to_excel

SUPPORTED_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.pdf'}


def read_images_from_folder(folder_path: str) -> list[str]:
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
            and os.path.splitext(f)[1].lower() in SUPPORTED_IMAGE_EXTENSIONS]


def pipeline(filepath: str, excel_path: str, start_row: int = 0):
    client = init_openai()

    images_paths = read_images_from_folder(filepath)

    print("\nStarting to extract data from ", images_paths, " at ", filepath, "...\n")

    list_of_dicts = []
    for path in images_paths:
        print(f"Processing {path}... ")

        print(f"\t> Extracting data... ", end="")
        raw_data_list = extract_data_from_image(client, path)
        print(f"({len(raw_data_list)} record(s) found) done")

        for i, raw_data in enumerate(raw_data_list):
            print(f"\t> Record {i + 1}/{len(raw_data_list)}: creating dictionary...", end="")
            raw_data_dict = create_dict_from_data(raw_data)
            print("done")

            print(f"\t> Record {i + 1}/{len(raw_data_list)}: cleaning data...", end="")
            data_dict = clean_data(raw_data_dict)
            print("done")

            list_of_dicts.append(data_dict)

        print(f"Completed processing {path}.\n")

    print("Extraction completed.")

    print("Saving to Excel at ", excel_path, "... ", end="")
    save_to_excel(excel_path, list_of_dicts, start_row=start_row)
    print("completed.\n")
