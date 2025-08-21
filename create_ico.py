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
    
    # Keep transparency for ICO (modern ICO format supports transparency)
    if img.mode == 'RGBA':
        # ICO can handle transparency, so keep it as is
        pass
    else:
        # Convert to RGBA if it's not already
        img = img.convert('RGBA')
    
    # Save as ICO
    ico_path = "images/favicon.ico"
    img.save(ico_path, format='ICO')
    print(f"Created {ico_path}")

if __name__ == "__main__":
    create_ico()
