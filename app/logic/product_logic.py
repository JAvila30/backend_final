from app.models import Product
from app.BC_Status import BCStatus
from app.utils.exceptions import BusinessException
from http import HTTPStatus
import uuid


def get_all():
    try:
        product = list(Product.objects.values())
        if len(product) > 0:
            response = BCStatus.SUCESS.code ,BCStatus.SUCESS.description , HTTPStatus.OK ,product
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

def get_one(product_id):
    try:
        product = list(Product.objects.filter(product_id=product_id).values())
        if len(product) > 0:
            product = product[0]
            response = BCStatus.SUCESS.code ,BCStatus.SUCESS.description , HTTPStatus.OK,  product
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

def save_product(request):
    product_data = request
    product_uuid = uuid.uuid4()
    try:
        Product.objects.create(prod_uuid=product_uuid, 
                               cli_uuid=product_data["body"]['cli_uuid'], 
                                prod_name=product_data["body"]['name'], 
                                container_uuid=product_data["body"]['container_uuid'], 
                                prod_harvest_date=product_data["body"]['harvest_date'],
                                prod_type=product_data["body"]['type'],
                                prod_qty=product_data["body"]['prod_qty'])
               
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

def update_product(request, product_id):
    product_data = request
    try:
        products = list(Product.objects.filter(prod_uuid=product_id).values())
        if len(products) > 0:
            product = Product.objects.get(prod_uuid=product_id)
            product.cli_uuid=product_data["body"]['cli_uuid']
            product.container_uuid=product_data["body"]['container_uuid']
            product.prod_name=product_data["body"]['name']
            product.prod_harvest_date=product_data["body"]['harvest_date']
            product.prod_type=product_data["body"]['type']
            product.prod_qty=product_data["body"]['prod_qty']
            product.save()
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

def delete_product(id):
    try:
        products = list(Product.objects.filter(prod_uuid=id).values())
        if len(products) > 0:
            Product.objects.filter(prod_uuid=id).delete()
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

