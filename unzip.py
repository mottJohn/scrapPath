import os, zipfile

dir_name = r"C:\Users\CHA82870\OneDrive - Mott MacDonald\Documents\scrapPath\pathConc_zip"
dir_extract = r"C:\Users\CHA82870\OneDrive - Mott MacDonald\Documents\scrapPath\pathConc"
extension = ".zip"

os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dir_extract) # extract file to dir
        zip_ref.close() # close file