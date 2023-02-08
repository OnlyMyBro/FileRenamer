import os

folder_path = input("Enter folder path:")

files = os.listdir(folder_path)

new_prefix = input("Enter new prefix for all files:")
rename_suffix = input("Enter new suffix (e.g. '_number'):")

i = 1
for file in files:
    os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_prefix + rename_suffix + str(i).zfill(len(str(len(files)))) + os.path.splitext(file)[1]))
    i += 1
