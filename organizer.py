import os
import shutil

# احفظي المسار الذي تريدين تنظيمه (غيري المسار لمجلد تجريبي لديكِ)
folder_path = os.path.expanduser("~/Downloads")

print("جاري تنظيم المجلد...")

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    
    # التجاوز إذا كان المجلد وليس ملف
    if os.path.isdir(file_path):
        continue
        
    name, ext = os.path.splitext(file)
    ext = ext[1:].lower() # معرفة امتداد الملف
    
    if ext == '':
        continue
        
    target_dir = os.path.join(folder_path, ext)
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        
    shutil.move(file_path, os.path.join(target_dir, file))

print("تم تنظيم المجلد بنجاح!")