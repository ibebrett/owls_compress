import base64

from .base import Compressor


class Base64Compressor(Compressor):
    def compress(self, txt):
        return base64.b64encode(txt)

    def uncompress(self, txt):
        return base64.b64decode(txt)
