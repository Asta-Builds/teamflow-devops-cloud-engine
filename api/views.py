# Automated Backend Service for [QA & Verification] Test Suite for hello in this project we build a iac with django and react
from rest_framework.views import APIView
from rest_framework.response import Response

class QaverificationtestsuitefView(APIView):
    def get(self, request):
        return Response({'status': 'active', 'ticket_id': 145})