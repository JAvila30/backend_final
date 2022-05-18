from app.BC_Status import BCStatus
from app.utils.exceptions import BusinessException
from http import HTTPStatus
from app.models import User
from django.contrib.auth.hashers import check_password

def login_request(request):
        print("inicio de login_request")
        try:
            print(request)
            user=request['username']
            plain_password=request['password']
            results = User.objects.filter(user_name=user).values()
            if len(results) > 0:
                data = results[0]
                encrypt_password = data['user_password']
                if check_password(plain_password,encrypt_password):
                    user_response = {
                        'user_info':{
                            "id": data['user_uuid'], 
                            "username": data['user_name'],
                            "email": data['user_email']
                        },
                        "user_role": data['user_role']
                        }
                    response = BCStatus.SUCESS.code ,BCStatus.SUCESS.description , HTTPStatus.OK ,user_response
                else:
                    response = BCStatus.INVALID_USER_OR_PASSWORD.code ,BCStatus.INVALID_USER_OR_PASSWORD.description , HTTPStatus.BAD_REQUEST ,None
            else:
                response = BCStatus.INVALID_USER_OR_PASSWORD.code ,BCStatus.INVALID_USER_OR_PASSWORD.description , HTTPStatus.BAD_REQUEST ,None
        except Exception as e:
            print(e)
            raise BusinessException(
                BCStatus.LOGIN_FAILED.code ,
                BCStatus.LOGIN_FAILED.description,
                HTTPStatus.INTERNAL_SERVER_ERROR,
                e
            )
        print("fin de login_request")
        return response

def logout_request(request):
        try:
            response = BCStatus.SUCESS.code ,BCStatus.SUCESS.description , HTTPStatus.OK, None
        except Exception as e:
            print(e)
            raise BusinessException(
                BCStatus.LOGIN_FAILED.code ,
                BCStatus.LOGIN_FAILED.description,
                HTTPStatus.INTERNAL_SERVER_ERROR,
                e
            )
        return response