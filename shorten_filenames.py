import os

def shorten_filenames(folder, max_length=100):
    for root, dirs, files in os.walk(folder):
        for file_name in files:
            if len(file_name) > max_length:
                old_path = os.path.join(root, file_name)
                name, ext = os.path.splitext(file_name)
                new_name = name[:max_length - len(ext)] + ext
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed: {file_name} -> {new_name}")

# Example usage
shorten_filenames("./projektnaNaloga/text_data")
