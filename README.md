# Automatic Image Enhancer

This project automatically enhances images using computer vision techniques. It utilizes the **CLAHE (Contrast Limited Adaptive Histogram Equalization)** algorithm to intelligently adjust brightness and contrast based on the image's specific characteristics.

## Features
*   **Automatic Enhancement:** Analyzes image brightness and applies optimal contrast/brightness adjustments.
*   **Web Interface:** Modern, user-friendly web app built with Streamlit.
*   **CLI Support:** Command-line tool for quick batch processing or scripting.
*   **Format Support:** Works with standard image formats (JPG, PNG, JPEG).

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/rohxn08/Automatic-Image-Enhancer.git
    cd "Automatic Image Enhancer"
    ```

2.  **Install required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Web Interface (Recommended)
Launch the interactive web application to upload, view, and download enhanced images.

```bash
streamlit run app.py
```
*The app will open in your default web browser.*

### 2. Command Line Interface
Run the script directly in your terminal.

```bash
python main1.py
```
*   Enter the path to your image when prompted.
*   Enter 'q' to quit.
*   The enhanced image will be saved in the same directory with `_enhanced` appended to the filename.

## Demo Results

Here are some examples of the automatic enhancement in action:

| Original Image | Enhanced Image |
| :---: | :---: |
| **Low Contrast / Dark** | **Brightened & Sharpened** |
| ![Original Eyes](Demo%20images/Eyes.jpg) | ![Enhanced Eyes](Demo%20images/Eyes_enhanced.jpg) |
| ![Original Scene](Demo%20images/images.jpeg) | ![Enhanced Scene](Demo%20images/images_enhanced.jpeg) |

---
*Built with OpenCV, NumPy, and Streamlit.*
