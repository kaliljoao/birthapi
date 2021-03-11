import swisseph as swe
from django.http.response import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view


class MainViewSet(viewsets.ModelViewSet):

    @api_view(['POST'])
    def GetUserBirthMap(request):
        user_map = {
            "Sun": [0, 0],
            "Mon": [1, 0],
            "Mer": [2, 0],
            "Ven": [3, 0],
            "Mar": [4, 0],
            "Jup": [5, 0],
            "Sat": [6, 0],
            "Ura": [7, 0],
            "Nep": [8, 0],
            "Plu": [9, 0],
            "Asc": [],     # pos [1][0]
            "MC":  [],     # pos [1][1]
            "Chi": [],     # 15 arq auxiliares
            "Nod": [10, 0]
        }
        julian = swe.julday(request.data['year'], request.data['month'], request.data['day'])
        for planet in user_map:

            if (user_map[planet] != []):
                user_map[planet][1] = swe.calc_ut(julian, user_map[planet][0])[0][0]
        return JsonResponse(user_map, safe=False)
