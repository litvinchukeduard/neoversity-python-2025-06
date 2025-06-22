from pathlib import Path

current_folder = Path('.')
folder_structure = list(current_folder.iterdir())
print(folder_structure)

print(list(folder_structure[0].iterdir()))


