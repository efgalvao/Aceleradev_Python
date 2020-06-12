import datetime

class LastSeen(object):

    def process_request(self, request):
        user = request.user
        if not user.is_authenticated():
            return None
        up = user.get_profile()
        up.last_login = datetime.now()
        up.save()
        return None