# Image Resizer

Resizes the image according to given new width and/or height, or scale.

# Quick Start
Script should be run by Python3.5

Example of run on Linux
```bash
python3 image_resize.py images.png --scale 1.5 -o resized_image.png
```

In case only width or only height is provided, than another dimension will be 
calculated proportionally to original image.

```bash
python3 image_resize.py images.png --width 500
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
