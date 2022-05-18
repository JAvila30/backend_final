from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.utils.exceptions import BusinessException
from app.utils import util
import json
from app.logic import user_logic

# Create your views here.
class UserView(View):
    print("inicio de UserView")
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        print("inicio de get")
        try:
            if (id != 0):
                code, description, httpstatus,execution_result = user_logic.get_one(id)
                response = util.build_response(code,description,httpstatus,execution_result)
            else:
                code, description, httpstatus, execution_result = user_logic.get_all()
                response = util.build_response(code,description,httpstatus,execution_result)
        except BusinessException as exception:
            response = util.build_response(
                exception.code, 
                exception.description,
                exception.httpstatus,
                None
                )
        print("fin de get")
        return response
    
    def post(self,request):
        print("inicio de post")
        try:
            json_payload = json.loads(request.body)
            code, description, httpstatus,execution_result = user_logic.save(json_payload)
            response = util.build_response(code,description,httpstatus,execution_result)
        except BusinessException as exception:
            response = util.build_response(
                exception.code, 
                exception.description,
                exception.httpstatus,
                None
                )
        print("fin de post")
        return response
        