import os
import pandas as pd
from argparse import ArgumentParser

def hdf_demo(infile_path):

    available_tables = []
    with pd.HDFStore(infile_path) as hdf:
        keys = hdf.keys()
        available_tables = [os.path.basename(key) for key in keys]
    
    for name in available_tables:
        print("- " * 60)
        print(name)
        data = pd.read_hdf(infile_path, key = name, start = 0, stop = 10)
        print(data)

if __name__ == "__main__":

    parser = ArgumentParser(description = "show events contained in this file")
    parser.add_argument("--infile", action = "store", dest = "infile_path")
    args = vars(parser.parse_args())

    hdf_demo(**args)
