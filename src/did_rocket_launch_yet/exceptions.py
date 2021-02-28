

class NgrokProxyConnectionError(Exception):
    """
    This exception will be raised when ngrok can't give a public url
    """

    def __init__(self):
        super().__init__("Ngrok has not provided a valid public url")
