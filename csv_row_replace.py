import pandas as pd
import numpy as np


def csv_row_replace(df, cep):
    cep = int(cep)
    for i in range(len(df.iloc[4])):
        df.iloc[4,i] = cep*i


if __name__ == '__main__':
    import sys
    import os
    input_path, cep = sys.argv[1], sys.argv[2]
    df = pd.read_csv(input_path)
    input_path = os.path.splitext(input_path)[0]
    csv_row_replace(df, cep)
    df.to_csv(input_path+".csv", index=None)
