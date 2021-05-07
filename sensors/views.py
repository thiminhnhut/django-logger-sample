from sensors.models import SensorSchema
from rest_framework.response import Response
from rest_framework.views import APIView
from marshmallow import ValidationError, EXCLUDE
from rest_framework.status import *
import logging

logger = logging.getLogger(__name__)


class Sensors(APIView):
    def post(self, request):
        try:
            sensor = SensorSchema().load(request.data, unknown=EXCLUDE)
            return Response(status=HTTP_200_OK)
        except ValidationError as error:
            return Response(error.messages, HTTP_400_BAD_REQUEST)
