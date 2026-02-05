import os
from django.db import models

# Project Model

class BlueprintProject(models.Model):
    project_name = CharField(max_length=100, unique=True)

    owner = model.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL
        related_name='blueprint_projects'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# Create your models here.
class VPSImage(models.Model):
    image_name=models.CharField(max_length=50)
    image_path=models.CharField(max_length=300)
    os_type=models.CharField(max_length=30) # rocky linux, rehel, ubuntu, ... and others
    ram_size= models.IntegerField()
    cpu_cnt=models.IntegerField()
    disk_size=models.IntegerField()


class OSParam(models.Model):
    # ForeginKey
    vps_image = models.ForeignKey(
        VPSImage,
        on_delete=models.CASCADE,
        related_name='op_params'
    )

    param_name=models.CharField(max_length=50)
    param_value=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.vps_image.image_name} - {self.param_name}"

class VPSUser(models.Model):
    username= models.CharField(max_length=50)
    user_id=models.CharField(max_length=32)
    password=models.CharField(max_length=100)
    primary_group=models.CharField(max_length=32)


class PreInstalledDriver(models.Model):
    driver_name=models.CharField(max_length=50)
    dirver_file_dir=models.CharField(max_length=50)
    insatlled_dir=models.CharField(max_length=100)
    driver_version=models.CharField(max_length=25)







class SubNet(models.Model):
    subnet_name = models.CharField(max_length=50)

class VPSNetworkInterface(models.Model):
    iface_name = models.CharField(max_length=50) #interface 이름
    



class Node(models.Model):
    node_name = models.CharField(max_length=50)
    node_ip = models.CharField(max_length=30)
    node_auth = models.CharField(max_length=10) # ssh, 등등 연결 방식

    def edit_ip(new_ip):
        node_ip = new_ip

