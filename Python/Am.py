import urllib.parse


class code:

    @staticmethod
    def decode(text):
        return urllib.parse.unquote(text)

