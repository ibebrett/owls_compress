from typing import List

import argparse
from dataclasses import dataclass
from .base import Compressor
from .compressors import compressors
from .datasets import datasets


def length_ratio(compressed: str, uncompressed: str) -> float:
    assert len(compressed) != 0
    return len(uncompressed) / len(compressed)


def bulk_compress(compressor: Compressor, texts: List[bytes]) -> List[bytes]:
    ret = [compressor.compress(t) for t in texts]
    assert all([isinstance(r, bytes) for r in ret])
    return ret

def bulk_uncompress(compressor: Compressor, texts: List[bytes]) -> List[bytes]:
    ret = [compressor.uncompress(t) for t in texts]
    assert all([isinstance(r, bytes) for r in ret])
    return ret



@dataclass
class EvalResult:
    txts: List[bytes]
    compressed: List[bytes]
    uncompressed: List[bytes]

    success: List[bool]
    all_success: bool

    scores: List[float]
    mean_score: float


def simple_eval(compressor: Compressor, txts: List[bytes]):
    scores = []
    compressed = bulk_compress(compressor, txts)
    uncompressed = bulk_uncompress(compressor, compressed)

    success = [c == u for (c, u) in zip(compressed, uncompressed)]
    all_success = all(success)

    scores = [length_ratio(c, u) for (c, u) in zip(compressed, uncompressed)]
    mean_score = sum(scores) / len(scores)

    return EvalResult(
        txts=txts,
        compressed=compressed,
        uncompressed=uncompressed,
        all_success=all_success,
        success=success,

        scores=scores,
        mean_score=mean_score,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('compressor', choices=compressors.keys())
    parser.add_argument('dataset', choices=datasets.keys())
    
    args = parser.parse_args()

    compressor = compressors[args.compressor]()
    dataset = datasets[args.dataset]
    result = simple_eval(compressor, dataset)

    print(result)
    

if __name__ == '__main__':
    main()
