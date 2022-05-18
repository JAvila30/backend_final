from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from utils.exceptions import BusinessException
from utils import util
from logic import container_logic
import json
from rest_framework import generics, permissions

# Create your views here.


class ContainerView(View):
    print("inicio de ContainerView")
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        print("inicio de getContainer")

        try:
            if (id != 0):
                code, description, httpstatus,container_result = container_logic.getOneContainer(id)
                response = util.build_response(code,description,httpstatus,container_result)
            else:
                code, description, httpstatus, container_result = container_logic.getAllContainer()
                response = util.build_response(code,description,httpstatus,container_result)
        except BusinessException as exception:
            response = util.build_response(
                exception.code, 
                exception.description,
                exception.httpstatus,
                None
                )
        print("fin de postContainer")
        return response
    
    def put(self, request,id):
        print("inicio de update Container")
        try:
            json_payload = json.loads(request.body)
            print(json_payload)
            code, description, httpstatus, container_execution = container_logic.update_container(json_payload,id)
            response = util.build_response(code,description,httpstatus,container_execution)
        except BusinessException as exception:
            print(exception)
            response = util.build_response(
                exception.code, 
                exception.description,
                exception.httpstatus,
                None
                )
        print("fin de update Container")
        return response
        
        
    def post(self, request):
        print("inicio de postContainer")
        try:
            json_payload = json.loads(request.body)
            print(json_payload)
            code, description, httpstatus = container_logic.save_container(json_payload)
            response = util.build_response(code,description,httpstatus,None)
        except BusinessException as exception:
            response = util.build_response(
                exception.code, 
                exception.description,
                exception.httpstatus,
                None
                )
        print("fin de postContainer")
        return response

    def delete(sef,request,id):
        print("inicio de delete Container")
        try:
            print("Id a elminar: ", id)
            code, description, httpstatus, container_status= container_logic.delete_container(id)
            response = util.build_response(code,description,httpstatus,container_status)
        except BusinessException as exception:
            response = util.build_response(
                exception.code, 
                exception.description,
                exception.httpstatus,
                None
                )
        print("fin de delete Container")
        return response
    