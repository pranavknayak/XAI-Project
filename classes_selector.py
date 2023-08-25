import random
from typing import List
import numpy as np
np.random.seed(42)


# Randomly samples 15 synsets from ImageNet
def synset_selector1k(filename: str='./LOC_synset_mapping.txt', debug:bool=False) -> List[int]:
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        classes = np.random.randint(low=0, high=1000, size=(15,))
        if debug:
            print(f"(class_id, synset_id, synset)")
            print()
            for id in classes:
                print(id, end="\t")
                print(f"{lines[int(id)][:9]}\t{lines[int(id)][9:]}")
            print()
        return classes.tolist()

# Randomly samples 15 synsets with only a single class per synset from ImageNet
def class_selector1k(filename: str='./LOC_synset_mapping.txt', debug:bool=False) -> List[int]:
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        classes = []
        while len(classes) < 15:
            idx = random.randint(0, 999)
            mapping = lines[idx]
            if ',' in mapping:
                continue
            classes.append(idx)
        if debug:
            print(f"(class_id, synset_id, synset)")
            print()
            for id in classes:
                print(id, end="\t")
                print(f"{lines[int(id)][:9]}\t{lines[int(id)][9:]}")
            print()
        return classes

# Randomly samples 15 synsets from ImageNet100
def synset_selector100(filename: str='./imagenet100labels.txt', debug:bool=False) -> List[int]:
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        classes = np.random.randint(low=0, high=100, size=(15,))
        if debug:
            print(f"(class_id, synset_id, synset)")
            print()
            for id in classes:
                print(id, end="\t")
                print(f"{lines[int(id)][:9]}\t{lines[int(id)][9:]}")
            print()
        return classes.tolist()

# Randomly samples 15 synsets with a single class per synset from ImageNet100
def class_selector100(filename: str='./LOC_synset_mapping.txt', debug:bool=False) -> List[int]:
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        classes = []
        while len(classes) < 15:
            idx = random.randint(0, 100)
            mapping = lines[idx]
            if ',' in mapping:
                continue
            classes.append(idx)
        if debug:
            print(f"(class_id, synset_id, synset)")
            print()
            for id in classes:
                print(id, end="\t")
                print(f"{lines[int(id)][:9]}\t{lines[int(id)][9:]}")
            print()
        return classes

if __name__ == "__main__":
    synset_selector100(debug=True)
    class_selector100(debug=True)
