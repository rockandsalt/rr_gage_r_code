import pandas as pd
import numpy as np

from itertools import product

def load_iso_data():

    data = pd.read_excel('./data/green_sample_benchmark.xls', sheet_name = 'archimedes', index_col= [0,1])
    iso_density = pd.read_excel('./data/green_sample_benchmark.xls', sheet_name = 'arch_param', index_col= 0)

    density_df = pd.DataFrame(columns = ['batch', 'id', 'density', 'operator', 'powder'])

    # density of stainless steel 316L (g/cc) taken from data sheet
    den_ss316 = 8.0

    unique_id = 0

    # iterate over each sample to do cartesian product
    for idx in data.index.unique():
        sample = data.loc[idx]

        op = int(np.unique(sample['operator']).squeeze())
        powder = str(np.unique(sample['powder type']).squeeze())
        batch = idx[0]

        d_weight = sample['dry weight'].to_numpy()
        wc_weight = sample['wet coated'].to_numpy()
        c_weight = sample['coated weight'].to_numpy()

        exp_num = sample['exp']
        # density of liquid taken from datasheet
        iso_den = iso_density.loc[exp_num].to_numpy()
        
        # cartesian product
        prod = product(d_weight, wc_weight, c_weight, iso_den)

        for d_w, wc_w, c_w, iso_d in prod:
            #compute true density refer to equation on top
            den = (d_w/(c_w - wc_w)*iso_d)/den_ss316*100
            new_entry = {
                'batch' : batch,
                'id' : unique_id,
                'density' : float(den.squeeze()),
                'operator' : op,
                'powder' : powder
            }

            density_df = density_df.append(new_entry, ignore_index = True)
        
        unique_id += 1
    
    return density_df