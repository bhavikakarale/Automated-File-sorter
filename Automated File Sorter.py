import os, shutil

path = r'give dir path'

file_name = os.listdir(path)

# make folder with the following names
folder_names = ['text files', 'excel files', 'image files']
for loop in (0, 3):
    os.mkdir(path+folder_names[loop])

for file in file_name:
    if '.csv' in file and not os.path.exists(path+'excel files/'+file):
        shutil.move(path+file, path+'excel files/'+file)
    elif '.txt' in file and not os.path.exists(path+'text files/'+file):
        shutil.move(path+file, path+'text files/'+file)
    elif '.png' in file and not os.path.exists(path+'image files/'+file):
        shutil.move(path+file, path+'image files/'+file)

