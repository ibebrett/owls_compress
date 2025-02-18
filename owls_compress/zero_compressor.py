from .base import Compressor


class ZeroCompressor(Compressor):
    def compress(self, txt: bytes) -> bytes:
        return txt

    def uncompress(self, txt: bytes) -> bytes:
        return txt


