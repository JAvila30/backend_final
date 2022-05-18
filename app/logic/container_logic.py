from app.models import Container
from app.BC_Status import BCStatus
from app.utils.exceptions import BusinessException
from http import HTTPStatus
import uuid
import json

def getAllContainer():
    try:
        container = list(Container.objects.values())
        if len(container) > 0:
            response = BCStatus.SUCESS.code ,BCStatus.SUCESS.description , HTTPStatus.OK ,container
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

def getOneContainer(container_id):
    print("inicio de getOneContainer")
    try:
        containers = list(Container.objects.filter(container_uuid=container_id).values())
        if len(containers) > 0:
            container = containers[0]
            response = BCStatus.SUCESS.code ,BCStatus.SUCESS.description , HTTPStatus.OK,  container
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
    print("Fin de getOneContainer")
    return response

def save_container(request):
    container_data = request
    container_id = uuid.uuid4()
    try:
        Container.objects.create(container_id=container_id, 
                                 max_capacity=container_data["body"]['max_capacity'], 
                                 current_capacity=container_data["body"]['current_capacity'],
                                 temperature=container_data["body"]['temperature'],
                                 type=container_data["body"]['type'])
        response =  BCStatus.SUCESS.code , BCStatus.SUCESS.description, HTTPStatus.OK
    except Exception as e:
        print(e)
        raise BusinessException(
            BCStatus.BD_ERROR.code ,
            BCStatus.BD_ERROR.description,
            HTTPStatus.BAD_REQUEST,
            e
        )
    return response

def update_container(request, container_id):
    container_data = request
    try:
        containers = list(Container.objects.filter(container_id=container_id).values())
        if len(containers) > 0:
            container = Container.objects.get(container_id=container_id)
            container.max_capacity = container_data["body"]['max_capacity']
            container.current_capacity = container_data["body"]['current_capacity']
            container.temperature = container_data["body"]['temperature']
            container.type = container_data["body"]['type']
            container.save()
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


def delete_container(container_id):
    try:
        containers = list(Container.objects.filter(container_uuid=container_id).values())
        if len(containers) > 0:
            Container.objects.filter(container_uuid=container_id).delete()
            response = BCStatus.SUCESS.code ,BCStatus.SUCESS.description , HTTPStatus.OK,  None
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