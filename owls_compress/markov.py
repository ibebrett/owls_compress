from typing import List, Iterator, Tuple
from collections import defaultdict

def get_character_slices(txts: List[bytes], n: int) -> Iterator[bytes]:
    for t in txts:
        if len(t) < n:
            continue
    
        for i in range(len(t) - n):
            yield t[i: i+n+1]


def max_key(dct):
    s = sorted([(v, k) for k, v in dct.items()])
    # s should be a list of number, string
    return s[-1][1]

class MarkovChain:
    def __init__(self, txts: List[bytes], n: int):
        self.table = defaultdict(lambda: defaultdict(int))
        self.z = defaultdict(int)
        self.no_prefix = defaultdict(int)

        # build the table.
        for s in get_character_slices(txts, n):
            prefix = s[:n-1]
            last = s[n:n+1]
            self.z[prefix] += 1
            self.table[prefix][last] += 1
            self.no_prefix[last] += 1

        assert self.no_prefix, "at least some text was processed."


    def max_sample(self, prefix: Tuple[bytes]) -> bytes | None:
        if prefix not in self.table:
            return None
        return max_key(self.table[prefix])
    


