from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from collections import Counter



@api_view(["POST"])
def lambda_function(request):
    try:
        quest=request.data.get('question')
        response=_ordenar(quest)
        return Response(response, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

def _ordenar(n):
    solution = [item for items, c in Counter(n).most_common() 
                                      for item in [items] * c] 
    res = {}
    res['solution'] = solution
    return res