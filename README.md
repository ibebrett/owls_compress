# OWLS Compress

## Setup

This code is setup like a real python package. To develop locally, install it with pip. Make sure you are in the root directory of
the repo.

```pip install -e . ```

This will let you import ```owls_compress``` anywhere you are using the same python interpreter. This is how real python packages work.
The one small difference is we pass the flag ```-e```. This tells pip to use this local folder as the source for the package, rather
than moving it to common location. This lets us continue developing the module locally and still use it as a "global" package.

## Running evals

To run an eval you can run the following script anywhere:

```owls_compress_evaluate ZeroCompressor train_shakespeare```

replacing with the compressor of your choice and the dataset of your choice.

We haven't cleaned up the code yet, but in the mess of the output you should see your score as the average percentage you
reduced by. We may introduce better and new metrics over time.

## Task

Your job is to implement a compression algorithm for William Shakespeare. We have 3 datasets prepared for you:

```(python)
from ows_compress.datasets import datasets

datasets['train_shakespeare'] # Use this to inform your compression algo
datasets['valid_shakespeare'] # Use this to test out your compression algo
datasets['test_shakespeare'] # This is the held out data we will use to judge the algos. Don't cheat and look at this :).
```

## Ideas

Run Length Encoding
Prediction by Partial Matching
Huffman Trees
Just use chatgpt?
... (plenty more)
