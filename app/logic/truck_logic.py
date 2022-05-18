from api.models import Truck
from api.BC_Status import BCStatus
from api.utils.exceptions import BusinessException
from http import HTTPStatus
import uuid
import json


def get_all():
    try:
        result = list(Truck.objects.values())
        if len(result) > 0:
            response = BCStatus.SUCESS.code ,BCStatus.SUCESS.description , HTTPStatus.OK ,result
        else:
            response = BCStatus.NOT_FOUND.code , BCStatus.NOT_FOUND.description, HTTPStatus.NOT_FOUND,None
    except Exception as e:
        print(e)
        raise BusinessException(
            BCStatus.BD_ERROR.code ,
            BCStatus.BD_ERROR.description,
            HTTPStatus.BAD_REQUEST,
            e
        )
    return response

def get_one(id):
    try:
        results = list(Truck.objects.filter(tru_uuid=id).values())
        if len(results) > 0:
            result = results[0]
            response = BCStatus.SUCESS.code ,BCStatus.SUCESS.description , HTTPStatus.OK,  result
        else:
            response =  BCStatus.NOT_FOUND.code , BCStatus.NOT_FOUND.description,HTTPStatus.NOT_FOUND, None
    except Exception as e:
        print(e)
        raise BusinessException(
            BCStatus.BD_ERROR.code ,
            BCStatus.BD_ERROR.description,
            HTTPStatus.BAD_REQUEST,
            e
        )
    return response

def save(request):
    data = request
    gen_uuid = uuid.uuid4()
    try:
        validation = validate_new_truck(data)
        if validation["isValid"]:
            Truck.objects.create(tru_uuid=gen_uuid, 
                                tru_max_capacity=data["body"]['tru_max_cap'], 
                                tru_actual_capacity=data["body"]['tru_actual_cap'], 
                                tru_location=data["body"]['tru_location'], 
                                tru_status=data["body"]['tru_status'],
                                tru_placa=data["body"]['tru_placa'],
                                tru_model=data["body"]['tru_model'],
                                tru_color=data["body"]['tru_brand'],
                                tru_truck_number=data["body"]['tru_color'],
                                tru_brand=data["body"]['tru_number'])
            response = validation['code'],  validation['description'], HTTPStatus.OK, None
        else:
            response =   validation['code'],  validation['description'], HTTPStatus.BAD_REQUEST, None
    except Exception as e:
        print(e)
        raise BusinessException(
            BCStatus.BD_ERROR.code ,
            BCStatus.BD_ERROR.description,
            HTTPStatus.BAD_REQUEST,
            e
        )
    return response

def update(request, id):
    data = request
    try:
        results = list(Truck.objects.filter(cli_uuid=id).values())
        if len(results) > 0:
            result = Truck.objects.get(cli_uuid=id)
            result.tru_max_capacity=data["body"]['tru_max_cap']
            result.tru_actual_capacity=data["body"]['tru_actual_cap']
            result.tru_location=data["body"]['tru_location'],
            result.tru_status=data["body"]['tru_status']
            result.tru_placa=data["body"]['tru_placa']
            result.tru_model=data["body"]['tru_model']
            result.tru_color=data["body"]['tru_brand']
            result.tru_truck_number=data["body"]['tru_color']
            result.tru_brand=data["body"]['tru_number']
            
            result.save(update_fields=["cli_first_name",
                                       "cli_last_name",
                                       "cli_age",
                                       "cli_document",
                                       "cli_document_type",
                                       "cli_cellphone",
                                       "cli_email","cli_direction"])
            response = BCStatus.SUCESS.code ,BCStatus.SUCESS.description , HTTPStatus.OK,  None
        else:
            response = BCStatus.NOT_FOUND.code , BCStatus.NOT_FOUND.description, HTTPStatus.NOT_FOUND,None
    except Exception as e:
        print(e)
        raise BusinessException(
            BCStatus.BD_ERROR.code ,
            BCStatus.BD_ERROR.description,
            HTTPStatus.BAD_REQUEST,
            e
        )
    return response

def delete(id):
    try:
        results = list(Truck.objects.filter(tru_uuid=id).values())
        if len(results) > 0:
            Truck.objects.filter(tru_uuid=id).delete()
            response = BCStatus.SUCESS.code ,BCStatus.SUCESS.description , HTTPStatus.OK,  None
        else:
            response = BCStatus.NOT_FOUND.code , BCStatus.NOT_FOUND.description,HTTPStatus.NOT_FOUND, None
    except Exception as e:
        print(e)
        raise BusinessException(
            BCStatus.BD_ERROR.code ,
            BCStatus.BD_ERROR.description,
            HTTPStatus.BAD_REQUEST,
            e
        )
    return response

def validate_new_truck(request):
    print("Inicio de validate_new_truck", request)
    try:
        trucks = list(Truck.objects.all().values())
        print(len(trucks))
        if len(trucks)>0:
            for truck in trucks:
                if request['body']['tru_placa'] == truck['tru_placa']:
                    code = BCStatus.DUPLICATED_PLAQUE_TRUCK_NUMBER.code
                    description = BCStatus.DUPLICATED_PLAQUE_TRUCK_NUMBER.description
                    isValid = False
                    response = {"isValid": isValid, "description": description, "code": code}
                    break
                elif request['body']['tru_number'] == truck['tru_truck_number']:
                    code = BCStatus.DUPLICATED_TRUCK_NUMBER.code
                    description = BCStatus.DUPLICATED_TRUCK_NUMBER.description
                    isValid = False
                    response = {"isValid": isValid, "description": description, "code": code}
                    break
                else:
                    code = BCStatus.SUCESS.code
                    description = BCStatus.SUCESS.description
                    isValid = True
                    response = {"isValid": isValid, "description": description, "code": code}
        else:
            code = BCStatus.SUCESS.code
            description = BCStatus.SUCESS.description
            isValid = True
            response = {"isValid": isValid, "description": description, "code": code}
        return response
    except Exception as e:
        print(e)
        raise BusinessException(
            BCStatus.FATAL_ERROR.code ,
            BCStatus.FATAL_ERROR.description,
            HTTPStatus.BAD_REQUEST,
            e)



  
