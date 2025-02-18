from typing import List

import os

data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")


datasets_files = {
    'raw_shakespeare': 'tiny_shakespeare.txt',
    'train_shakespeare': 'shake_train.txt',
    'valid_shakespeare': 'shake_valid.txt',
    'test_shakespeare': 'shake_test.txt',
}

def read_dataset(path: str) -> List[bytes]:
     with open(path, 'r') as f:
        lines = f.readlines()
        return [l.encode(encoding='ascii', errors='ignore') for l in lines]
            

datasets = {
    k: read_dataset(os.path.join(data_path, v)) for (k, v) in datasets_files.items()
}
