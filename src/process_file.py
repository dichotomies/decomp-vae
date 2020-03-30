
import h5py
import time


import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--i1', type=int)
parser.add_argument('--i2', type=int)
args = parser.parse_args()

t1 = time.time()

import os
os.makedirs('test', exist_ok=True)


import shelve

i2 = min(args.i2, 737280)

with h5py.File('dsprites-dataset/dsprites_ndarray_co1sh3sc6or40x32y32_64x64.hdf5', 'r') as f:
    with shelve.open('test/slice_{}_{}'.format(args.i1, i2)) as f_shelve:
        imgs = {i: None for i in range(args.i1, i2)}
        for i in range(args.i1, i2):
            imgs[i] = (f['imgs'][i])
            if i % 50 == 0:
                print(i)
        f_shelve['imgs'] = imgs

t2 = time.time()

print('Time taken: {}'.format(t2 - t1))
