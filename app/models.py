from django.db import models
import datetime
class Container(models.Model):
    container_uuid=models.CharField(max_length=64)
    max_capacity=models.IntegerField(default=0)
    current_capacity=models.IntegerField(default=0)
    temperature=models.IntegerField(default=0)
    type=models.IntegerField(default=0)

class ContainerType(models.Model):
    container_type_id=models.IntegerField(default=0)
    type=models.CharField(max_length=64)
    
class Client(models.Model):
    cli_uuid=models.CharField(max_length=64)
    cli_first_name=models.CharField(max_length=64)
    cli_last_name=models.CharField(max_length=64)
    cli_age=models.IntegerField(default=0)
    cli_document=models.CharField(max_length=64,default=None)
    cli_document_type=models.CharField(max_length=16)
    cli_cellphone=models.CharField(max_length=32)
    cli_email=models.CharField(max_length=64)
    cli_direction=models.CharField(max_length=248)

class Product(models.Model):
    cli_uuid=models.CharField(max_length=64)
    container_uuid=models.CharField(max_length=64)
    prod_uuid=models.CharField(max_length=64)
    prod_name=models.CharField(max_length=64)
    prod_register_date=models.DateTimeField(default=datetime.datetime.now)
    prod_harvest_date=models.DateField()
    prod_type=models.CharField(max_length=64)
    prod_qty=models.FloatField()
    
class User(models.Model):
    user_uuid=models.CharField(max_length=64)
    user_name=models.CharField(max_length=32, null=True)
    user_password=models.CharField(max_length=128)
    user_email=models.CharField(max_length=64)
    user_direction=models.CharField(max_length=248)
    user_cellphone=models.CharField(max_length=32)
    user_role=models.IntegerField()
    
class UserType(models.Model):
    userT_id=models.IntegerField()
    userT_role=models.CharField(max_length=32)

class Truck(models.Model):
    tru_uuid=models.CharField(max_length=64,null=True)
    tru_max_capacity=models.IntegerField()
    tru_actual_capacity=models.IntegerField()
    tru_location=models.CharField(max_length=84)
    tru_status=models.CharField(max_length=32)
    tru_placa=models.CharField(max_length=32)
    tru_brand=models.CharField(max_length=32)
    tru_model=models.CharField(max_length=32)
    tru_color=models.CharField(max_length=32)
    tru_truck_number=models.CharField(max_length=32)

class TruckType(models.Model):
    truT_id=models.IntegerField()
    truT_type=models.CharField(max_length=32)


    
    
    
    
