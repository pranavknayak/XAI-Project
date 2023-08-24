import random
from typing import List
import numpy as np
np.random.seed(42)

def synset_selector(filename: str='./LOC_synset_mapping.txt', debug:bool=False) -> List[int]:
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

def class_selector(filename: str='./LOC_synset_mapping.txt', debug:bool=False) -> List[int]:
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


if __name__ == "__main__":
    class_selector(debug=True)
    synset_selector(debug=True)
