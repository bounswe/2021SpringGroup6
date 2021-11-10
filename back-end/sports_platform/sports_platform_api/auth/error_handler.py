from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    
    response = exception_handler(exc, context)
    if(response.data['detail'].code == 'authentication_failed'):
        response.data['message'] = "Invalid token."
        del response.data['detail']

    return response
