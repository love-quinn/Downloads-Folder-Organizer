import sys
import os
import shutil

def get_current_user():
    username = os.getenv("USERNAME")
    print(f"Current username: {username}")

def listen_organize():
    if len(sys.argv) < 2:
        print("Usage: python automation.py <directory_to_be_sorted_path>")
        sys.exit(1)
    # The path of the directory to be sorted
    path = sys.argv[1]
    # This populates a list with the filenames in the directory
    list_ = os.listdir(path)

    # Traverses every file
    for file_ in list_:
        name, ext = os.path.splitext(file_)
        # Stores the extension type
        ext = ext[1:]
        # If it is a directory, it forces the next iteration
        if ext == '':
            continue
        # if a directory with the name 'ext' exists,
        # it moves the file to that directory
        if os.path.exists(path+'/'+ext):
            shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
        # If the directory does not exist, it creates a new directory
        else:
            os.makedirs(path+'/'+ext)
            shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
    
def main():
    import time
    # get_current_user()
    # while True:
    try:
        listen_organize()
    except Exception as e:
        print(e)
        # time.sleep(30)
        # listen_organize()

main()
