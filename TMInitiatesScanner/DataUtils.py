import os
from PIL import Image


def images_to_pdf(folder: str, output_path: str) -> None:
    """Bundle all images in a folder into a single PDF.

    Args:
        folder:      Path to the folder containing the images.
        output_path: Full path and name of the output PDF (e.g. "output/result.pdf").

    Example:
        images_to_pdf("scans/", "output/meditators.pdf")
    """
    supported_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.tiff'}

    image_files = [
        f for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f))
           and os.path.splitext(f)[1].lower() in supported_extensions
    ]

    if not image_files:
        print(f"No images found in '{folder}'")
        return

    images = [
        Image.open(os.path.join(folder, f)).convert("RGB")
        for f in image_files
    ]

    first, *rest = images

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    first.save(output_path, save_all=True, append_images=rest)
    print(f"PDF saved to: {output_path} ({len(images)} pages)")


def image_to_pdf_each(folder: str, output_folder: str) -> None:
    """Convert each image in a folder to an individual PDF, keeping the original filename.

    Args:
        folder:        Path to the folder containing the images.
        output_folder: Path to the folder where the PDFs will be saved.

    Example:
        image_to_pdf_each("scans/", "output/pdfs/")
        # scans/form_a.jpg  -> output/pdfs/form_a.pdf
        # scans/form_b.png  -> output/pdfs/form_b.pdf
    """
    supported_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.tiff'}

    image_files = [
        f for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f))
           and os.path.splitext(f)[1].lower() in supported_extensions
    ]

    if not image_files:
        print(f"No images found in '{folder}'")
        return

    os.makedirs(output_folder, exist_ok=True)

    for filename in image_files:
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder, f"{base_name}.pdf")

        image = Image.open(os.path.join(folder, filename)).convert("RGB")
        image.save(output_path)

        print(f"  {filename} -> {output_path}")


def rename_files(folder: str, name: str, n: int = 4) -> None:
    """Rename files in a folder alphabetically using a zero-padded index.

    Args:
        folder: Path to the folder containing the files.
        name:   Base name for the renamed files (e.g. "meditator").
        n:      Number of digits for zero-padding (e.g. 4 → "0001").

    Example:
        rename_files("scans/", name="meditator", n=4)
        # renames files to: meditator-0001.jpg, meditator-0002.jpg, ...
    """
    files = [
        f for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f))
    ]

    for index, filename in enumerate(files, start=1):
        ext = os.path.splitext(filename)[1]
        new_name = f"{name}-{str(index).zfill(n)}{ext}"
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
        print(f"  {filename} -> {new_name}")
