import os
import glob

# For social files
for file_path in glob.glob('social/**/*.md', recursive=True) + glob.glob('confirmed_speaker/**/*.md', recursive=True) + ['confirmed_speaker/generate_linkedin_posts.py']:
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        
        new_content = content.replace("10:00 AM", "09:00 AM")
        
        if new_content != content:
            with open(file_path, 'w') as f:
                f.write(new_content)
            print("Updated", file_path)

# For website files
for file_path in glob.glob('website/**/*.html', recursive=True):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        
        new_content = content.replace("10:00 – 18:00 IST", "09:00 – 18:00 IST")
        
        if new_content != content:
            with open(file_path, 'w') as f:
                f.write(new_content)
            print("Updated", file_path)
