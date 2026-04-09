import zipfile
import os
import sys

def create_zip():
    zip_name = 'ecart++=+.zip'
    print(f"Creating {zip_name} ...")
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk('.'):
            # Exclude unwanted directories
            if 'venv' in dirs:
                dirs.remove('venv')
            if '__pycache__' in dirs:
                dirs.remove('__pycache__')
            if '.git' in dirs:
                dirs.remove('.git')
            if 'node_modules' in dirs:
                dirs.remove('node_modules')
            
            # Add files to zip
            for file in files:
                if file == zip_name or file == 'zip_project.py' or file.endswith('.db'):
                    # skip backing up the large database or the script itself
                    if file == zip_name or file == 'zip_project.py':
                        continue
                
                file_path = os.path.join(root, file)
                # print(f"Adding {file_path}")
                zipf.write(file_path)
                
    print(f"Successfully created {zip_name}")

if __name__ == '__main__':
    create_zip()
