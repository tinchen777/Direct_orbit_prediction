import numpy as np

filename = ('results/star_0117_Transformer_star_s_ftM_sl848_ll212_pl212_dm512_nh8_el2_dl1_df2048_fc1_ebtimeF_dtTrue_test_0/'
            'metrics.npy')
data = np.load(filename)
print(data)
print(len(data))
print(data.shape)