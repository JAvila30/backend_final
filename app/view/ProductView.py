from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.utils import util
from app.logic import product_logic
from app.utils.exceptions import BusinessException
import json


class ProductView(View):
    print("inicio de ProductView")
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        print("inicio de get Product")
        try:
            if (id != 0):
                code, description, httpstatus, execution_response = product_logic.get_one(id)
                response = util.build_response(code ,description, httpstatus, execution_response)
            else:
                code, description, httpstatus, execution_response = product_logic.get_all()
                response = util.build_response(code, description, httpstatus, execution_response)
        except BusinessException as exception:
            print(exception)
            response = util.build_response(
                exception.code, 
                exception.description,
                exception.httpstatus,
                None
                )
        print("fin de get Product")
        return response
    
    def post(self, request):
            print("inicio de post Product")
            try:
                json_payload = json.loads(request.body)
                print(json_payload)
                code, description, httpstatus, execution_response = product_logic.save_product(json_payload)
                response = util.build_response(code,description,httpstatus,execution_response)
            except BusinessException as exception:
                print(exception)
                response = util.build_response(
                    exception.code, 
                    exception.description,
                    exception.httpstatus,
                    None
                    )
            print("fin de post Product")
            return response
    
    def put(self, request,id):
        print("inicio de update Product")
        try:
            json_payload = json.loads(request.body)
            print(json_payload)
            code, description, httpstatus, execution_response = product_logic.update_product(json_payload,id)
            response = util.build_response(code,description,httpstatus,execution_response)
        except BusinessException as exception:
            print(exception)
            response = util.build_response(
                exception.code, 
                exception.description,
                exception.httpstatus,
                None
                )
        print("fin de update Product")
        return response
    
    def delete(sef,request,id):
        print("inicio de delete Product")
        try:
            print("Id a elminar: ", id)
            code, description, httpstatus, execution_response = product_logic.delete_product(id)
            response = util.build_response(code,description,httpstatus,execution_response)
        except BusinessException as exception:
            print(exception)
            response = util.build_response(
                exception.code, 
                exception.description,
                exception.httpstatus,
                None
                )
        print("fin de delete Product")
        return response