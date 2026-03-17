import os
import glob

# For all html files outside website
for file_path in glob.glob('**/*.html', recursive=True):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        
        new_content = content.replace("09:00 – 18:00 IST", "09:00 – 18:00 IST")
        
        if new_content != content:
            with open(file_path, 'w') as f:
                f.write(new_content)
            print("Updated", file_path)

# For python files
for file_path in glob.glob('**/*.py', recursive=True):
    if 'update_timings.py' in file_path: continue
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        
        new_content = content.replace("09:00 – 18:00 IST", "09:00 – 18:00 IST")
        
        if new_content != content:
            with open(file_path, 'w') as f:
                f.write(new_content)
            print("Updated", file_path)

# For tex and md files
for file_path in glob.glob('**/*.tex', recursive=True) + glob.glob('**/*.md', recursive=True):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        
        new_content = content.replace("10:00 -- 18:00 IST", "09:00 -- 18:00 IST")
        new_content = new_content.replace("10:00 -- 10:30 & Inauguration", "09:00 -- 09:30 & Inauguration")
        new_content = new_content.replace("10:00 – 10:30   | **Inauguration**", "09:00 – 09:30   | **Inauguration**")

        if new_content != content:
            with open(file_path, 'w') as f:
                f.write(new_content)
            print("Updated", file_path)
