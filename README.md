Here's a README.md file to explain the usage of your AI Photo Editor application and how to install the required Python packages.

# AI Photo Editor

AI Photo Editor is a Python-based application for basic photo editing using filters like grayscale, contrast adjustment, edge detection, and a cartoon effect. The application provides an easy-to-use graphical interface built with Tkinter.

## Features

- *Open and Save Images*: Open images in .jpg, .jpeg, and .png formats and save them after editing.
- *Apply Filters*: Supports the following filters:
  - Grayscale
  - Contrast adjustment
  - Edge Detection
  - Cartoon Effect

## Prerequisites

Ensure that you have Python installed (Python 3.6 or later is recommended).

## Installation

1. Clone the repository or download the project files.
2. Install the required Python packages.

To install the packages, open your terminal or command prompt and run the following:

bash
pip install pillow opencv-python-headless numpy


This will install:
- *Pillow*: For handling and editing images.
- *OpenCV*: For computer vision tasks (edge detection and cartoon effect).
- *NumPy*: For image array manipulation.

## How to Run the Application

1. Navigate to the project directory.
2. Run the following command:

   bash
   python ai_photo_editor.py
   

## Usage Instructions

1. *Open Image*: Click the "Open Image" button to select an image file (JPG, JPEG, or PNG format).
2. *Apply Filters*: Choose a filter from the filter buttons. The selected filter will be applied to the opened image and displayed on the canvas.
3. *Save Image*: Click the "Save Image" button to save the edited image.

## File Structure

- **ai_photo_editor.py**: Main script for the application.
- **README.md**: Instructions and documentation for the project.

## Example

The main screen provides buttons for opening, saving, and applying filters to the image. Here’s how the application interface looks:


[ Open Image ] [ Save Image ]
----------------------------
|          Canvas          |
|         for Image        |
----------------------------
[   Grayscale    ][ Contrast ]
[ Edge Detection ][ Cartoon ]


## License

This project is licensed under the MIT License.
