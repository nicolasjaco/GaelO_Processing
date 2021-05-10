from django.http import HttpResponseServerError, JsonResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponse
from django.views.defaults import page_not_found
from django.shortcuts import render
from django.core import exceptions


def handler_404(request, exception):  
    status='404' 
    print('js suis ici')
    return JsonResponse({status:'ErrorMessage: '+exception})
    # return HttpResponseNotFound('ErrorMessage: '+ exception)

def handler_400(request,exception): 
    status='400' 
    return JsonResponse({status:'ErrorMessage: '+exception})       
    # return HttpResponseBadRequest('ErrorMessage: ' + exception)

def handler_500(request):
    status='500' 
    return JsonResponse({status:'Server Error'})
    # return HttpResponseServerError('Server Error')

    #test : (bof)
    # response = render_to_response(context_instance=RequestContext(request))
    # response.status_code = 500
    # return response
    




