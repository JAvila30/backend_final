from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from app.utils.exceptions import BusinessException
from app.utils import util
from app.logic import client_logic
import json

# Create your views here.

class ClientView(View):
    print("inicio de ClientView")
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        print("inicio de get")
        try:
            if (id != 0):
                code, description, httpstatus,execution_result = client_logic.get_one(id)
                response = util.build_response(code,description,httpstatus,execution_result)
            else:
                code, description, httpstatus, execution_result = client_logic.get_all()
                response = util.build_response(code,description,httpstatus,execution_result)
        except BusinessException as exception:
            print(exception)
            response = util.build_response(
                exception.code, 
                exception.description,
                exception.httpstatus,
                None
                )
        print("fin de get")
        return response
    
    def put(self, request,id):
        print("inicio de update ")
        try:
            json_payload = json.loads(request.body)
            print(json_payload)
            code, description, httpstatus, execution_result = client_logic.update(json_payload,id)
            response = util.build_response(code,description,httpstatus,execution_result)
        except BusinessException as exception:
            print(exception)
            response = util.build_response(
                exception.code, 
                exception.description,
                exception.httpstatus,
                None
                )
        print("fin de update ")
        return response
        
        
    def post(self, request):
        print("inicio de post")
        try:
            json_payload = json.loads(request.body)
            print(json_payload)
            code, description, httpstatus, execution_response = client_logic.save(json_payload)
            response = util.build_response(code,description,httpstatus,execution_response)
        except BusinessException as exception:
            print(exception)
            response = util.build_response(
                exception.code, 
                exception.description,
                exception.httpstatus,
                None
                )
        print("fin de post")
        return response

    def delete(sef,request,id):
        print("inicio de delete ")
        try:
            print("Id a elminar: ", id)
            code, description, httpstatus, execution_result= client_logic.delete(id)
            response = util.build_response(code,description,httpstatus,execution_result)
        except BusinessException as exception:
            print(exception)
            response = util.build_response(
                exception.code, 
                exception.description,
                exception.httpstatus,
                None
                )
        print("fin de delete ")
        return response
    