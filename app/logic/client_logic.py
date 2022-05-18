from app.models import Client
from app.BC_Status import BCStatus
from app.utils.exceptions import BusinessException
from http import HTTPStatus
import uuid
import json


def get_all():
    try:
        result = list(Client.objects.values())
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
        results = list(Client.objects.filter(cli_uuid=id).values())
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
        Client.objects.create(cli_uuid=gen_uuid, 
                               cli_first_name=data["body"]['first_name'], 
                                 cli_last_name=data["body"]['last_name'], 
                                 cli_age=data["body"]['age'], 
                                 cli_document=data["body"]['document'],
                                 cli_document_type=data["body"]['document_type'],
                                 cli_cellphone=data["body"]['cellphone'],
                                 cli_email=data["body"]['email'],
                                 cli_direction=data["body"]['direction'])
        response =  BCStatus.SUCESS.code , BCStatus.SUCESS.description, HTTPStatus.OK, None
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
        results = list(Client.objects.filter(cli_uuid=id).values())
        if len(results) > 0:
            result = Client.objects.get(cli_uuid=id)
            result.cli_first_name=data["body"]['first_name'] 
            result.cli_last_name=data["body"]['last_name']
            result.cli_age=data["body"]['age']
            result.cli_document=data["body"]['document']
            result.cli_document_type=data["body"]['document_type']
            result.cli_cellphone=data["body"]['cellphone']
            result.cli_email=data["body"]['email']
            result.cli_direction=data["body"]['direction']
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
        results = list(Client.objects.filter(cli_uuid=id).values())
        if len(results) > 0:
            Client.objects.filter(cli_uuid=id).delete()
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

