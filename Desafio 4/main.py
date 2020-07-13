import jwt

def create_token(data:dict, secret:str) -> str:
    """
    Creates a token with JWT(JSON Web Token)

    Parameters:
    data: dict
        Data to encode.
    secret: str
        Secret key to encode and decode.

    Return:
    token: str
        JSON Web Token.
    """
    token = jwt.encode(data, secret, algorithm='HS256')
    return token

def verify_signature(token:str/bytes) -> dict:
    """
    Decodes the given token

    Parameters:
    token: str/bytes
        Token to be decoded.

    Return:
    token: dict
        The decoded message.
    """
    key = 'acelera'
    try:
        x = jwt.decode(token, key, algorithms=['HS256'])
    except:
        return {'error': 2}
    return x
