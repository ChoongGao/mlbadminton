import os
import pandas as pd
import numpy as np

for root,dir,files in os.walk('./raw_data/clear'):
    for name in files:
        print(name)
        df = pd.read_csv(os.path.join(root, name))
        print(df.head)


# print(df.head)
# print(df['ax(g)'].max())