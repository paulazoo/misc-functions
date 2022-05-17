import os
base_dir = 'F:/2p/stephen/'
mouse = 'SZ879'
date = '220516'
num_folders = 16

do_flim_folders = True

# F:/2p/stephen/SZ885/220508_SZ885/220508_SZ885_run1
folder_base = base_dir+mouse+'/'+date+'_'+mouse+'/'+ date + '_' + mouse + '_run'
# F:/2p/stephen/SZ885/220508_SZ885/FLIM/220508_SZ885_run1
flim_folder_base = base_dir+mouse+'/'+date+'_'+mouse+'/'+'FLIM/'+ date + '_' + mouse + '_run'

print(folder_base)

folder_nums = [i for i in range(1,num_folders+1)]
for folder_num in folder_nums:
    total_path = folder_base + str(folder_num)
    # Check whether the specified path exists or not
    isExist = os.path.exists(total_path)
    print(isExist)
    if not isExist:
        # Create a new directory because it does not exist 
        os.makedirs(total_path)
        print("The new directory is created!")
    if do_flim_folders:
        flim_total_path = flim_folder_base + str(folder_num)
        if not os.path.exists(flim_total_path):
            os.makedirs(flim_total_path)
