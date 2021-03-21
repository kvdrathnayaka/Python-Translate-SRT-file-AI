"""
#######################################
    @ Author : The DemonWolf
#######################################

This is a python script that convert the languages. Simply put all the .srt files that need to convert,
into given "Input files" folder then run the program. Output files will be available
after end of the program in "Output files" folder.

The python script used Free Google Translate API for Python to translate the languages.
Translates totally free of charge.
"""

# Import necessary libraries
import glob
import os
import re

import translators as ts

# Run main method to execute the program
if __name__ == '__main__':
    Input_file_path = "Input files/"
    Output_file_path = "Output files/"
    file_names = []
    # Grab all the .srt files one by one in the Input files folder and open them
    for file in glob.glob(os.path.join(Input_file_path, '*.srt')):
        with open(file, 'r') as openfile:
            # Read file line by line
            lines = openfile.readlines()
            openfile.close()
            outfile = open("Output files/" + file.split("\\")[1], 'w', encoding="utf-8")
            for line in lines:
                if re.search('^[0-9]+$', line) is None and \
                        re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and \
                        re.search('^$', line) is None:
                    Trans = ts.google(line.rstrip('\n'), if_use_cn_host=True, from_language='auto', to_language='si')
                    print(line.rstrip('\n'), Trans)
                    line = Trans
                if not line.strip():
                    outfile.write("\n")
                outfile.write(line)
            outfile.close()
