import os
import shutil

src = r"C:\Users\shree\.gemini\antigravity\brain\5423f1bf-0124-4a7c-8fcc-e9c199054a2c\media__1780947557333.png"
dest_logo = r"E:\VPHS WEBSITE\media\school\logo.png"
dest_favicon = r"E:\VPHS WEBSITE\media\school\favicon.png"

if os.path.exists(src):
    os.makedirs(os.path.dirname(dest_logo), exist_ok=True)
    shutil.copy(src, dest_logo)
    shutil.copy(src, dest_favicon)
    print("Successfully copied user logo to media folders!")
else:
    print(f"Error: source logo file {src} not found!")
