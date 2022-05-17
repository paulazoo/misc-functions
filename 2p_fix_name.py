import os
from os.path import isfile, join
base_path = 'F:/2p/stephen/SZ885/220514_SZ885/FLIM'
# 220514_SZ885_run1_c1
all_files = [f for f in os.listdir(base_path) if isfile(join(base_path, f))]

base_path = 'F:/2p/stephen/SZ885/220514_SZ885/FLIM/'
for filename in all_files:
    new_filename = filename
    new_filename = filename[:5] + '4' + filename[6:]
    print(new_filename)
    os.rename(base_path+filename, base_path+new_filename)