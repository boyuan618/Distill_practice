# Refrences: https://www.geeksforgeeks.org/compare-two-files-line-by-line-in-python/
# Importing difflib
import difflib, glob, datetime


#Compare 2 most recent html files
html_names = list(glob.glob('screenshots/shielded-harbor-71309.herokuapp.com_login-pc/html/*.html'))[-2:]
print("Files:", len(html_names))

with open(html_names[0]) as file_1:
    file_1_text = file_1.readlines()
  
with open(html_names[1]) as file_2:
    file_2_text = file_2.readlines()
  
# Find and save the diff:
diff = ""
for line in difflib.unified_diff(file_1_text, file_2_text, fromfile='file1.txt', tofile='file2.txt', lineterm=''):
    diff += line + "\n"
    
if diff:  
    with open(f"defacement\\shielded-harbor-71309.herokuapp.com_login-pc\\html\\Changes detected at {datetime.datetime.now()}.txt".replace(":", "_"), "w+") as file:
        file.write(diff)


    

#Compare 2 most recent content files    
content_names = list(glob.glob('screenshots/shielded-harbor-71309.herokuapp.com_login-pc/content/*.txt'))[-2:]
print("Files:", len(content_names))

with open(content_names[0]) as file_1:
    file_1_text = file_1.readlines()
  
with open(content_names[1]) as file_2:
    file_2_text = file_2.readlines()
  
# Find and save the diff:
diff = ""
for line in difflib.unified_diff(file_1_text, file_2_text, fromfile='file1.txt', tofile='file2.txt', lineterm=''):
    diff += line +"\n"

if diff:
    with open(f"defacement\\shielded-harbor-71309.herokuapp.com_login-pc\\content\\Changes detected at {datetime.datetime.now()}.txt".replace(":", "_"), "w+") as file:
        file.write(diff)