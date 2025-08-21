#!/usr/bin/env python3
"""
Create favicon.ico file from PNG images.
"""

from PIL import Image
import os

def create_ico():
    """Create favicon.ico file with multiple sizes."""
    # Load the 32x32 PNG favicon
    png_path = "images/favicon-32x32.png"
    if not os.path.exists(png_path):
        print(f"Error: {png_path} not found!")
        return
    
    # Open the PNG image
    img = Image.open(png_path)
    
    # Convert to RGB if necessary (ICO doesn't support RGBA)
    if img.mode == 'RGBA':
        # Create a white background
        background = Image.new('RGB', img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[-1])  # Use alpha channel as mask
        img = background
    
    # Save as ICO
    ico_path = "images/favicon.ico"
    img.save(ico_path, format='ICO')
    print(f"Created {ico_path}")

if __name__ == "__main__":
    create_ico()
