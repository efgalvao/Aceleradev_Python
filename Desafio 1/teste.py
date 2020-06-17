from operator import itemgetter
import json
from collections import Counter
'''
@api_view(["POST"])
def lambda_function(questiondata):

    try:
        quest=json.loads(questiondata.body)
        quest=quest['question']
        answer=_ordenar(quest)
        return JsonResponse(answer, safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
'''

"""
def _ordenar(numbers):
    out = []
    nums = list(set([(a, numbers.count(a)) for a in numbers]))
    nums.sort(key=itemgetter(0))
    nums.sort(key=itemgetter(1), reverse=True)
    #nums.reverse()
    for n in nums:
        counter = n[1]
        while counter > 0:
            out.append(n[0])
            counter -= 1
    res = {}
    res['solution'] = out
    res1 = json.dumps(res)
    return res
    """
def _ordenar(n):
    solution = [item for items, c in Counter(n).most_common() 
                                      for item in [items] * c] 
    res = {}
    res['solution'] = solution
    res = json.dumps(res)
    return res

numbers = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12, 5]
numbers2 = [2, 3, 2, 4, 5, 12, 2, 3]
numbers3 = [2, 4, 2, 1, 2]
numbers4 = [6, 6, 6, 6, 6, 6, 2, 2, 2, 1, 4]
numbers5 = [3, 3, 3, 5, 3, 2, 4, 2, 2, 12, 12]
numbers6 = [2, 12, 2, 5, 2, 4, 3, 3]
numbers7 = [4, 12, 12, 5, 5, 2, 2, 2, 3, 3, 3, 3]
print(_ordenar(numbers7))