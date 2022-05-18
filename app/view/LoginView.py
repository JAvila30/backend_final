
from app.utils import util
from app.logic import login_logic
from app.utils.exceptions import BusinessException
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class LoginView(View):
    print("inicio de LoginView")
    ##@method_decorator(csrf_exempt)
    ##def dispatch(self, request, *args, **kwargs):
    ##    return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        print("inicio de post")
        try:
            json_payload = json.loads(request.body)
            code, description, httpstatus, execution_result = login_logic.login_request(json_payload)
            response = util.build_response(code,description,httpstatus,execution_result)
        except BusinessException as exception:
            print(exception)
            response = util.build_response(
                exception.code, 
                exception.description,
                exception.httpstatus,
                None
                )
        print("fin de LoginView ")
        return response

class LogOutView(View):
    print("inicio de LogOutView")

    def post(self, request):
        print("inicio de post")
        try:
            code, description, httpstatus, execution_result = login_logic.logout_request(request)
            response = util.build_response(code,description,httpstatus,execution_result)
        except BusinessException as exception:
            print(exception)
            response = util.build_response(
                exception.code, 
                exception.description,
                exception.httpstatus,
                None
                )
        print("fin de LogOutView ")
        return response