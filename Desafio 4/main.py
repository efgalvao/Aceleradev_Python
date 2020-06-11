import jwt

def create_token(data, secret):
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

def verify_signature(token):
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
    #err = {'error': 2}
    try:
        return jwt.decode(token, key, algorithms=['HS256'])
    except:
        return {'error': 2}
    #return x

print(create_token({'Oie': 123}, 'acelera'))
print(verify_signature(b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJPaWUiOjEyM30._vrN3OpjWoBX7MU9JaCakhBkeErGKF4vwVUKONwQpUg'
))