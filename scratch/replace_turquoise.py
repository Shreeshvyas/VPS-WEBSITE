import os

file_path = r"E:\VPHS WEBSITE\school\static\school\css\style.css"

if not os.path.exists(file_path):
    print("Error: style.css not found!")
    exit(1)

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Count occurrences of old colors
count_0d = content.lower().count("#0d9488")
count_0099 = content.lower().count("#0099b8")

print(f"Found {count_0d} instances of '#0d9488'")
print(f"Found {count_0099} instances of '#0099b8'")

# Perform case-insensitive replaces
content = content.replace("#0d9488", "#00afb9")
content = content.replace("#0d9488".upper(), "#00afb9")
content = content.replace("#0099b8", "#00afb9")
content = content.replace("#0099b8".upper(), "#00afb9")

# Also update the RGB coordinates for glow effects if needed
# #00afb9 in RGB is (0, 175, 185)
content = content.replace("0, 153, 184", "0, 175, 185")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Replaced colors with bright turquoise #00afb9 in style.css!")
