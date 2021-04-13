from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from apps.decrypt.utils import decrypt_message


@api_view(['POST'])
@parser_classes([JSONParser])
def decrypt(request):
    
    passphrase = request.data.get('passphrase')
    message = request.data.get('message')

    if passphrase is None:
        return Response({"detail": "Must provide passphrase and message"}, status=status.HTTP_400_BAD_REQUEST)

    if message is None:
        return Response({"detail": "Must provide passphrase and message"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        message = decrypt_message(passphrase, message)
        decrypted_message = str(message)
        return Response({"DecryptedMessage": decrypted_message}, status=status.HTTP_200_OK)
    except ValueError:
        return Response({"detail": "can not decrypt message! Incorrect passphrase or PGP encoded message."}, status=status.HTTP_400_BAD_REQUEST)
