#!/usr/bin/env python3
"""
Generate favicon files with "AP" in a circle using the theme color.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_favicon(size, output_path):
    """Create a favicon with the specified size."""
    # Create a new image with transparent background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Theme colors
    primary_color = (82, 173, 200)  # #52adc8
    border_color = (47, 127, 147)   # #2f7f93
    text_color = (255, 255, 255)    # White
    
    # Calculate circle parameters
    center = size // 2
    radius = (size // 2) - 2
    
    # Draw circle background
    draw.ellipse([center - radius, center - radius, 
                  center + radius, center + radius], 
                 fill=primary_color, outline=border_color, width=2)
    
    # Try to use a system font, fallback to default if not available
    try:
        # Try to find a suitable font
        font_size = int(size * 0.35)
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)
    except:
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
        except:
            font = ImageFont.load_default()
    
    # Draw "AP" text
    text = "AP"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = center - text_width // 2
    y = center - text_height // 2
    
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Save the image
    img.save(output_path, 'PNG')
    print(f"Created {output_path}")

def main():
    """Generate all favicon sizes."""
    # Create images directory if it doesn't exist
    images_dir = "images"
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
    
    # Generate different favicon sizes
    sizes = [
        (32, "favicon-32x32.png"),
        (192, "favicon-192x192.png"),
        (512, "favicon-512x512.png"),
        (180, "apple-touch-icon-180x180.png")
    ]
    
    for size, filename in sizes:
        output_path = os.path.join(images_dir, filename)
        create_favicon(size, output_path)
    
    print("Favicon generation complete!")

if __name__ == "__main__":
    main()
