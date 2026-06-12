import os

file_path = r"E:\VPHS WEBSITE\school\static\school\css\style.css"

if not os.path.exists(file_path):
    print("Error: style.css not found!")
    exit(1)

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update variables
old_light_vars = """    /* Light Theme (Ultra Premium Slate-Indigo) */
    --bg-primary: #f8fafc;
    --bg-secondary: #ffffff;
    --bg-tertiary: #f1f5f9;
    --text-primary: #0f172a;
    --text-secondary: #334155;
    --text-muted: #64748b;
    
    /* Curated Luxury Color Palette */
    --primary-color: #4f46e5;      /* Indigo */
    --primary-glow: rgba(79, 70, 229, 0.15);
    --primary-light: #e0e7ff;
    --primary-dark: #3730a3;
    
    --accent-color: #f59e0b;       /* Amber Gold */
    --accent-glow: rgba(245, 158, 11, 0.2);
    --accent-light: #fef3c7;
    
    --purple-glow: rgba(139, 92, 246, 0.15);
    --success-color: #10b981;
    --danger-color: #f43f5e;
    
    /* Layout & Glassmorphism */
    --border-color: rgba(99, 102, 241, 0.08);
    --card-bg: rgba(255, 255, 255, 0.7);
    --card-border: rgba(255, 255, 255, 0.6);
    --card-shadow: 0 10px 40px -15px rgba(79, 70, 229, 0.08), 0 1px 3px 0 rgba(79, 70, 229, 0.02);
    --card-shadow-hover: 0 25px 50px -12px rgba(79, 70, 229, 0.18), 0 4px 8px -2px rgba(79, 70, 229, 0.08);"""

new_light_vars = """    /* Light Theme (Ultra Premium Slate-Teal) */
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
    --card-bg: rgba(255, 255, 255, 0.75);
    --card-border: rgba(255, 255, 255, 0.65);
    --card-shadow: 0 10px 40px -15px rgba(var(--primary-glow-rgb), 0.06), 0 1px 3px 0 rgba(var(--primary-glow-rgb), 0.02);
    --card-shadow-hover: 0 25px 50px -12px rgba(var(--primary-glow-rgb), 0.15), 0 4px 8px -2px rgba(var(--primary-glow-rgb), 0.05);"""

old_dark_vars = """[data-theme="dark"] {
    --bg-primary: #030712;
    --bg-secondary: #0b0f19;
    --bg-tertiary: #111827;
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    
    --primary-color: #6366f1;
    --primary-glow: rgba(99, 102, 241, 0.25);
    --primary-light: #1e1b4b;
    --primary-dark: #818cf8;
    
    --accent-color: #fbbf24;
    --accent-glow: rgba(251, 191, 36, 0.25);
    --accent-light: #2d2204;
    
    --border-color: rgba(99, 102, 241, 0.15);
    --card-bg: rgba(11, 15, 25, 0.65);
    --card-border: rgba(255, 255, 255, 0.03);
    --card-shadow: 0 10px 40px -15px rgba(0, 0, 0, 0.5), 0 1px 3px 0 rgba(0, 0, 0, 0.2);
    --card-shadow-hover: 0 25px 50px -12px rgba(99, 102, 241, 0.25), 0 4px 12px 0 rgba(0, 0, 0, 0.3);
}"""

new_dark_vars = """[data-theme="dark"] {
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

content = content.replace(old_light_vars, new_light_vars)
content = content.replace(old_dark_vars, new_dark_vars)

# Replace other colors and glow shadows
content = content.replace("#8b5cf6", "#0ea5e9") # gradient end color -> sky blue
content = content.replace("rgba(79, 70, 229, 0.4)", "rgba(var(--primary-glow-rgb), 0.4)")
content = content.replace("rgba(79, 70, 229, 0.3)", "rgba(var(--primary-glow-rgb), 0.3)")
content = content.replace("rgba(79, 70, 229, 0.18)", "rgba(var(--primary-glow-rgb), 0.18)")
content = content.replace("rgba(79, 70, 229, 0.1)", "rgba(var(--primary-glow-rgb), 0.1)")
content = content.replace("rgba(99, 102, 241, 0.08)", "rgba(var(--primary-glow-rgb), 0.08)")
content = content.replace("rgba(99, 102, 241, 0.15)", "rgba(var(--primary-glow-rgb), 0.15)")
content = content.replace("rgba(99, 102, 241, 0.25)", "rgba(var(--primary-glow-rgb), 0.25)")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("style.css color variables and hex overrides successfully updated to Teal!")
