import json
from django.http import HttpResponseServerError, JsonResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponse
from django.views.defaults import page_not_found
from django.shortcuts import render
from django.core import exceptions


class GaelOException(Exception) :
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code
    
    def get_response(self) :
        return HttpResponse(json.dumps({'errorMessage:': self.args}),content_type='application/json; charset=utf-8')

class GaelOBadRequestException(GaelOException) :
    def __init__(self, message) :
        super().__init__(message, 400)

class GaelONotFoundException(GaelOException) :
    def __init__(self, message) :
        super().__init__(message, 404)
    




