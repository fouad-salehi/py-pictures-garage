# PyPicturesGarage

![Platform](https://img.shields.io/badge/platform-Desktop-blue?style=for-the-badge)
![Language](https://img.shields.io/badge/language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![Vision](https://img.shields.io/badge/vision-OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Math](https://img.shields.io/badge/math-NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Effects](https://img.shields.io/badge/effects-12%20Artistic-orange?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

## About

PyPicturesGarage is a desktop photo editing application built with Python and PyQt5 that turns ordinary photos into artistic images using OpenCV.
The project runs entirely offline, requires no external API, and gives the user full control over the editing pipeline: load an image, apply one of twelve artistic effects, rotate or crop it, and save the result.

> [!NOTE]
> **PyPicturesGarage provides a complete editing workflow:**
> - **Effects** — Twelve artistic and tonal filters including Oil Painting, Cartoon, Pencil Sketch, Watercolor, Vintage Film, HDR, Sharpen, Cool Tone, Warm Tone, Noir B&W, Vivid, and Bokeh.
> - **Transform** — Rotate 90° left/right, rotate 180°, and free-form crop by dragging on the preview.
> - **Export** — Save the final image as JPG or PNG with a single click.

The application uses a clean card-based light theme inspired by modern web design systems, with a splash screen, a home page, and a dedicated editor page managed through a stacked widget architecture.

## Screenshots

<p align="center">
  <img src="https://github.com/user-attachments/assets/e7443f56-2ff7-4ffa-9a51-48483a060b30" width="24%" style="border-radius: 12px;" />
  <img src="https://github.com/user-attachments/assets/5ed82e66-e378-4de3-ae27-93c2ec98d82b" width="24%" style="border-radius: 12px;" />
  <img src="https://github.com/user-attachments/assets/b7121d2a-a558-4755-941b-a897c6eada15" width="24%" style="border-radius: 12px;" />
  <img src="https://github.com/user-attachments/assets/a609479e-d6ff-43c4-838b-e4e62c21d8a8" width="24%" style="border-radius: 12px;" />
</p>

## Download

> [!TIP]
> **Ready-to-run executable:**
> [Download PyPicturesGarage.exe](https://github.com/fouad-salehi/py-pictures-garage/releases/download/v1.0.0/PyPicturesGarage.exe)
> 
>
> No Python installation required. Just download, run, and start editing.
> If you prefer to build from source, follow the installation steps below.

## Technologies

- Python 3
- PyQt5
- OpenCV
- NumPy
- Pillow
- Git and GitHub

## Libraries to Install

Open a terminal in the project folder and install the required packages with:

```bash
pip install PyQt5 opencv-python numpy pillow
```

If you prefer to install them one by one:

```bash
pip install PyQt5
pip install opencv-python
pip install numpy
pip install pillow
```

> [!WARNING]
> Make sure you have Python 3.8 or newer installed. It is recommended to use a virtual environment:
> ```bash
> python -m venv .venv
> .venv\Scripts\activate
> pip install PyQt5 opencv-python numpy pillow
> ```

## Features

- Load PNG, JPG, and BMP images
- Twelve artistic and tonal effects
- Rotate 90° left, 90° right, and 180°
- Free-form crop with live selection overlay
- Reset to the latest edited state
- Save result as JPG or PNG
- Clean light theme with card-based layout
- Fully offline, no API key required

## Project Structure

```
PyPicturesGarage/
├── README.md
├── LICENSE
├── requirements.txt
└── source/
    ├── main.py
    ├── effects.py
    ├── theme.py
    ├── splash.py
    ├── home.py
    ├── editor.py
    └── crop_label.py
```

## Installation

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt`, use the manual command shown in the Libraries to Install section.

## Run

```bash
python source/main.py
```

## Project

> [!TIP]
> **Repository:**
> https://github.com/fouad-salehi/py-pictures-garage

**Project Title:**
PyPicturesGarage – A Desktop Photo Editor with OpenCV Artistic Effects and PyQt5 Interface

PyPicturesGarage is developed as a personal project exploring the practical use of computer vision and desktop GUI development with Python.

## Author

[**Fouad Salehi**](https://github.com/fouad-salehi)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Libraries to Install

| Library | Purpose |
|---|---|
| **PyQt5** | Desktop GUI framework |
| **opencv-python** | Image processing and artistic effects |
| **numpy** | Numerical arrays used by OpenCV |
| **pillow** | Optional image format support |

One-line install:

```bash
pip install PyQt5 opencv-python numpy pillow
