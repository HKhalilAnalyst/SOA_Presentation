import numpy as np
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HousePrediction(APIView):
    def post(self, request):
        data = request.data
        Size = data['Size']
        Bedroom = data['Bedroom']
        lin_reg_model = ApiConfig.model
        House_price_prediction = lin_reg_model.predict([[Size, Bedroom]])[0][0]
        House_price_prediction = np.round(House_price_prediction, 1)
        response_dict = {"Predicted Price ($)": House_price_prediction}
        return Response(response_dict, status=200)