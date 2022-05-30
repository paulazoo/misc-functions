import os
base_dir = 'F:/2p/stephen/'
mouse = 'SZ879'
date = '220518'

# F:/2p/stephen/SZ885/220508_SZ885/220508_SZ885_run1
folder_base = base_dir+mouse+'/'+date+'_'+mouse+'/'+ date + '_' + mouse + '_run'
# F:/2p/stephen/SZ885/220508_SZ885/
gen_dir = base_dir+mouse+'/'+date+'_'+mouse+'/'

num_folders = 16
folder_nums = [i for i in range(1,num_folders+1)]
for folder_num in folder_nums:
    folder_name = folder_base + str(folder_num) +'/'
    # data files
    data_num_str = str(folder_num).zfill(3)
    ephys_data = mouse+'_'+date+'_'+data_num_str+'.ephys'
    matlab_data = mouse+'_'+date+'_'+data_num_str+'.mat'
    sbx_data = mouse+'_'+date+'_'+data_num_str+'.sbx'
    # move each file
    if os.path.exists(gen_dir+ephys_data):
        os.rename(gen_dir+ephys_data, folder_name+ephys_data)
    if os.path.exists(gen_dir+matlab_data):
        os.rename(gen_dir+matlab_data, folder_name+matlab_data)
    if os.path.exists(gen_dir+sbx_data):
        os.rename(gen_dir+sbx_data, folder_name+sbx_data)

