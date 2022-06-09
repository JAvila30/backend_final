import re
from app.models import User
from app.BC_Status import BCStatus
from app.utils.exceptions import BusinessException
from http import HTTPStatus
import uuid
from django.contrib.auth.hashers import make_password, check_password

def get_all():
    try:
        result = list(User.objects.values())
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
        results = list(User.objects.filter(user_uuid=id).values())
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

    try:
        user_name = data["body"]['user_name']
        validation = validate_new_user(data)
        print(validation)
        if validation['isValid']:
            gen_uuid = uuid.uuid4()
            encryptedpassword=make_password(data["body"]['user_pass'])
            User.objects.create(user_uuid=gen_uuid, 
                                user_name=data["body"]['user_name'], 
                                    user_password=encryptedpassword, 
                                    user_email=data["body"]['user_email'], 
                                    user_direction=data["body"]['user_dir'],
                                    user_cellphone=data["body"]['user_cellphone'],
                                    user_role=int(data["body"]['user_role']))
            response = validation['code'],  validation['description'], HTTPStatus.OK, user_name
        else:
            response =   validation['code'],  validation['description'], HTTPStatus.BAD_REQUEST, user_name
        return response
    except BusinessException as e:
        print(e)
    except Exception as e:
        print(e)
        raise BusinessException(
            BCStatus.BD_ERROR.code ,
            BCStatus.BD_ERROR.description,
            HTTPStatus.BAD_REQUEST,
            e
        )
   

def validate_new_user(request):
    #print("Inicio de validate_new_user", request)
    try:
        users = list(User.objects.all().values())
        if len(users)>0:
            for user in users:
                print( user['user_name'])
                if request['body']['user_name'] == user['user_name']:
                    print("primer if")
                    code = BCStatus.DUPLICATED_NAME_USER.code
                    description = BCStatus.DUPLICATED_NAME_USER.description
                    isValid = False
                    response = {"isValid": isValid, "description": description, "code": code}
                    break
                elif request['body']['user_email'] == user['user_email']:
                    print("segundor if")
                    code = BCStatus.DUPLICATED_EMAIL_USER.code
                    description = BCStatus.DUPLICATED_EMAIL_USER.description
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
        print("entre a la excepción")
        print(e)
        raise BusinessException(
            BCStatus.FATAL_ERROR.code ,
            BCStatus.FATAL_ERROR.description,
            HTTPStatus.BAD_REQUEST,
            e)



  
