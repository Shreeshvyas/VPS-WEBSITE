import os

file_path = r"E:\VPHS WEBSITE\school\static\school\css\style.css"

if not os.path.exists(file_path):
    print("Error: style.css not found!")
    exit(1)

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update variables
old_light_vars = """    /* Light Theme (Ultra Premium Slate-Teal) */
    --bg-primary: #f8fafc;
    --bg-secondary: #ffffff;
    --bg-tertiary: #f0fdfa; /* Soft Teal background */
    --text-primary: #0f172a;
    --text-secondary: #334155;
    --text-muted: #64748b;
    
    /* Curated Teal Color Palette */
    --primary-color: #0d9488;      /* Teal 600 */
    --primary-glow-rgb: 13, 148, 136;
    --primary-glow: rgba(13, 148, 136, 0.15);
    --primary-light: #ccfbf1;      /* Teal 100 */
    --primary-dark: #115e59;       /* Teal 800 */
    
    --accent-color: #d97706;       /* Warm Amber Gold */
    --accent-glow: rgba(217, 119, 6, 0.2);
    --accent-light: #fef3c7;
    
    --purple-glow: rgba(20, 184, 166, 0.15); /* Secondary light teal glow */
    --success-color: #10b981;
    --danger-color: #f43f5e;
    
    /* Layout & Glassmorphism */
    --border-color: rgba(13, 148, 136, 0.08);
    --card-bg: rgba(255, 255, 255, 0.7);
    --card-border: rgba(255, 255, 255, 0.6);
    --card-shadow: 0 10px 40px -15px rgba(var(--primary-glow-rgb), 0.06), 0 1px 3px 0 rgba(var(--primary-glow-rgb), 0.02);
    --card-shadow-hover: 0 25px 50px -12px rgba(var(--primary-glow-rgb), 0.15), 0 4px 8px -2px rgba(var(--primary-glow-rgb), 0.05);"""

new_light_vars = """    /* Light Theme (Ultra Premium Slate-Turquoise) */
    --bg-primary: #f8fafc;
    --bg-secondary: #ffffff;
    --bg-tertiary: #e0f7fa; /* Soft Turquoise background */
    --text-primary: #03252a;
    --text-secondary: #264a4f;
    --text-muted: #628286;
    
    /* Curated Turquoise Color Palette */
    --primary-color: #0099b8;      /* Turquoise/Teal Blue */
    --primary-glow-rgb: 0, 153, 184;
    --primary-glow: rgba(0, 153, 184, 0.15);
    --primary-light: #b2ebf2;      /* Turquoise 100 */
    --primary-dark: #006680;       /* Turquoise 800 */
    
    --accent-color: #d97706;       /* Warm Amber Gold */
    --accent-glow: rgba(217, 119, 6, 0.2);
    --accent-light: #fef3c7;
    
    --purple-glow: rgba(0, 180, 216, 0.15); /* Secondary turquoise glow */
    --success-color: #10b981;
    --danger-color: #f43f5e;
    
    /* Layout & Glassmorphism */
    --border-color: rgba(0, 153, 184, 0.08);
    --card-bg: rgba(255, 255, 255, 0.7);
    --card-border: rgba(255, 255, 255, 0.6);
    --card-shadow: 0 10px 40px -15px rgba(var(--primary-glow-rgb), 0.06), 0 1px 3px 0 rgba(var(--primary-glow-rgb), 0.02);
    --card-shadow-hover: 0 25px 50px -12px rgba(var(--primary-glow-rgb), 0.15), 0 4px 8px -2px rgba(var(--primary-glow-rgb), 0.05);"""

old_dark_vars = """[data-theme="dark"] {
    --bg-primary: #040d12;        /* Dark forest/teal void */
    --bg-secondary: #071916;      /* Tealish black */
    --bg-tertiary: #0b2420;
    --text-primary: #f2fbf9;
    --text-secondary: #a3c2be;
    --text-muted: #62827e;
    
    --primary-color: #2dd4bf;      /* Teal 400 */
    --primary-glow-rgb: 45, 212, 191;
    --primary-glow: rgba(45, 212, 191, 0.25);
    --primary-light: #0f463e;      /* Teal 800 equivalent */
    --primary-dark: #2dd4bf;
    
    --accent-color: #fbbf24;
    --accent-glow: rgba(251, 191, 36, 0.25);
    --accent-light: #2d2204;
    
    --border-color: rgba(45, 212, 191, 0.15);
    --card-bg: rgba(7, 25, 22, 0.7);
    --card-border: rgba(255, 255, 255, 0.03);
    --card-shadow: 0 10px 40px -15px rgba(0, 0, 0, 0.6), 0 1px 3px 0 rgba(0, 0, 0, 0.3);
    --card-shadow-hover: 0 25px 50px -12px rgba(var(--primary-glow-rgb), 0.22), 0 4px 12px 0 rgba(0, 0, 0, 0.4);
}"""

new_dark_vars = """[data-theme="dark"] {
    --bg-primary: #02161a;        /* Deep Turquoise black void */
    --bg-secondary: #052026;      /* Turquoise black */
    --bg-tertiary: #0a2d35;
    --text-primary: #e6f7f9;
    --text-secondary: #9ecad2;
    --text-muted: #5e8c95;
    
    --primary-color: #00b4d8;      /* Turquoise 400 */
    --primary-glow-rgb: 0, 180, 216;
    --primary-glow: rgba(0, 180, 216, 0.25);
    --primary-light: #004d60;      /* Turquoise 800 */
    --primary-dark: #00b4d8;
    
    --accent-color: #fbbf24;
    --accent-glow: rgba(251, 191, 36, 0.25);
    --accent-light: #2d2204;
    
    --border-color: rgba(0, 180, 216, 0.15);
    --card-bg: rgba(5, 32, 38, 0.7);
    --card-border: rgba(255, 255, 255, 0.03);
    --card-shadow: 0 10px 40px -15px rgba(0, 0, 0, 0.6), 0 1px 3px 0 rgba(0, 0, 0, 0.3);
    --card-shadow-hover: 0 25px 50px -12px rgba(var(--primary-glow-rgb), 0.22), 0 4px 12px 0 rgba(0, 0, 0, 0.4);
}"""

content = content.replace(old_light_vars, new_light_vars)
content = content.replace(old_dark_vars, new_dark_vars)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("style.css successfully updated to Turquoise theme!")
