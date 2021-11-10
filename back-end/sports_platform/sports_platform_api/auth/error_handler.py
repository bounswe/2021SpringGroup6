from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    if(response.data['detail'].code == 'authentication_failed'):
        #response.data['code'] = 401
        response.data['message'] = "Invalid token."
        del response.data['detail']

    return response
