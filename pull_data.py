import os

for root,dir,files in os.walk('../../Witmotion/Data'):
    print(root)
    for name in files:
        print(name)