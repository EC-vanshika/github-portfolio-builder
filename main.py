import tkinter as tk
from tkinter import filedialog, messagebox
from jinja2 import Environment, FileSystemLoader
import os

# Ensure required folders exist
os.makedirs('templates', exist_ok=True)
os.makedirs('output', exist_ok=True)

def upload_screenshot():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")])
    entry_screenshot.delete(0, tk.END)
    entry_screenshot.insert(0, path)

def generate_readme():
    selected_template = template_var.get()
    env = Environment(loader=FileSystemLoader('templates'))
    
    try:
        template = env.get_template(selected_template)
    except Exception as e:
        messagebox.showerror("Template Error", f"Template not found: {selected_template}")
        return

    data = {
        'project_name': entry_name.get(),
        'description': entry_desc.get(),
        'feature_1': entry_feat1.get(),
        'feature_2': entry_feat2.get(),
        'installation_steps': entry_install.get(),
        'tech_stack': entry_tech.get(),
        'github_link': entry_git.get(),
        'linkedin_link': entry_linkedin.get(),
        'screenshot': entry_screenshot.get()
    }

    output = template.render(data)
    preview_box.delete("1.0", tk.END)
    preview_box.insert(tk.END, output)

    with open('output/README.md', 'w') as f:
        f.write(output)

    messagebox.showinfo("Success", "README.md generated in output folder!")

# GUI Setup
root = tk.Tk()
root.title("GitHub Portfolio Builder")
root.geometry("800x750")

fields = [
    ("Project Name", "entry_name"),
    ("Description", "entry_desc"),
    ("Feature 1", "entry_feat1"),
    ("Feature 2", "entry_feat2"),
    ("Installation Steps", "entry_install"),
    ("Tech Stack", "entry_tech"),
    ("GitHub Link", "entry_git"),
    ("LinkedIn Link", "entry_linkedin"),
    ("Screenshot Path", "entry_screenshot")
]

entries = {}
for label_text, var_name in fields:
    frame = tk.Frame(root)
    frame.pack(pady=4)
    label = tk.Label(frame, text=label_text, width=18, anchor="w")
    label.pack(side="left")
    entry = tk.Entry(frame, width=60)
    entry.pack(side="left")
    entries[var_name] = entry

entry_name = entries["entry_name"]
entry_desc = entries["entry_desc"]
entry_feat1 = entries["entry_feat1"]
entry_feat2 = entries["entry_feat2"]
entry_install = entries["entry_install"]
entry_tech = entries["entry_tech"]
entry_git = entries["entry_git"]
entry_linkedin = entries["entry_linkedin"]
entry_screenshot = entries["entry_screenshot"]

# Screenshot Upload Button
upload_btn = tk.Button(root, text="Upload Screenshot", command=upload_screenshot)
upload_btn.pack(pady=5)

# Template Selector
template_frame = tk.Frame(root)
template_frame.pack(pady=5)
tk.Label(template_frame, text="Select Template Style:").pack(side="left")
template_var = tk.StringVar(value="basic_readme.txt")
template_options = ["basic_readme.txt", "emoji_readme.txt", "minimal_readme.txt"]
template_menu = tk.OptionMenu(template_frame, template_var, *template_options)
template_menu.pack(side="left")

# Generate Button
generate_btn = tk.Button(root, text="Generate README", command=generate_readme, bg="#4CAF50", fg="white", height=2, width=30)
generate_btn.pack(pady=10)

# Preview Box
tk.Label(root, text="Live Preview:").pack()
preview_box = tk.Text(root, height=15, width=95)
preview_box.pack(pady=10)

root.mainloop()


