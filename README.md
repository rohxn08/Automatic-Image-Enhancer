Automatic Image Enhancer

This project automatically enhances images using computer vision techniques and a CLAHE(Contrast Limited Adaptive Histogram Equalization) algorithm only based on brightness and contrast of the image.

Features:
Automatic Image Enhancement 
Supports all the different Image formats and sizes

Uses OpenCV and Numpy libraries to enhance an inputted Image

Installation:

1. Cloning the repository from github:
```bash
git clone https://github.com/your-username/automatic-image-enhancer.git
```
2. Installing the required packages from requirements.txt:
```bash
pip install -r requirements.txt
```

3. Usage: run the main1.py file by-
```bash
python main1.py
```
Followed by entering the image that you want to enhance and if you want to exit the program then enter 'q'.
Note that enhanced image appears as a seperate image in the same directory with the original image name appended with '_enhanced'.


Demo Output:
Images before enhancement:
![Image before enhancement](Demo%20images/Eyes.jpg)
![Image before enhancement](Demo%20images/images.jpeg)

Images after enhancement:
![Image after enhancement](Demo%20images/Eyes_enhanced.jpg)
![Image after enhancement](Demo%20images/images_enhanced.jpeg)



