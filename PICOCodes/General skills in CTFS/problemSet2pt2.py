# picoGym problem set 2

# -first grep
# -first find
# -big zip


# 1) first grep
# Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way.
# used grep
# grep -i "pico" file

# 2) first find
# Unzip this archive and find the file named 'uber-secret.txt'
# Download zip file

# next run find -name 'uber-secret.txt' then copy path and nano the text file which will get you your code

# 3) big zip

# used grep to look at all files in the directory and subdirectories. You have to use a period at the end of grep

# grep -i -r "pico" * .
