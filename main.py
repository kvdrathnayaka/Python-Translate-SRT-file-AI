import glob
import os
import re

import translators as ts

if __name__ == '__main__':
    Input_file_path = "Input files/"
    Output_file_path = "Output files/"
    file_names = []
    for file in glob.glob(os.path.join(Input_file_path, '*.srt')):
        with open(file, 'r') as openfile:
            # read file line by line
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
