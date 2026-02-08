from django.db.models.fields import AutoField


from django.db.models.fields.related import ForeignKey
from django.conf import settings

from typing import Any


import os
from django.db import models
from django.contrib.auth.models import AbstractUser # 이 임포트가 중요합니다!
# Project Model

class AethraPrintProject(models.Model):
    project_name = models.CharField(max_length=100, unique=True)
    owner_id = models.IntegerField()

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

class Vswitch(models.Model):
    switch_name = models.CharField(max_length=50)

class VyOSContainer(models.Model):
    vy_name = models.CharField(max_lenght=50)

class VPSNetworkInterface(models.Model):
    iface_name = models.CharField(max_length=50) #interface 이름
    

class Gns3Server(models.Model):
    gns3_ip = models.CharFiled(max_length=50)
    gns3_port = models.IntegerField()

class Gns3Project(models.Model):
    project_name = models.CharField(max_length=50)

class VPS(models.Model):
    pass

class Node(models.Model):
    node_name = models.CharField(max_length=50)
    node_ip = models.CharField(max_length=30)
    node_auth = models.CharField(max_length=10) # ssh, 등등 연결 방식

    project = models.ForeignKey(
        AethraPrintProject,
        on_delete=models.CASCADE,
        related_name='nodes' # 프로젝트들이 각 node를 가짐.
    )


class VPSMetric(models.Model):
    pass


class SSLCert(models.Model): 
    name = ""
    file_type = " " #root ca or wildcard cert, or web site cert
    password = models.TextField() #  인증서를 갖고 오기 위한 비번
    #cert_type =
    #file_name =  # 암호화된 cert 파일 이름

class SSHPublicKey(models.Model):
    key_id = models.AutoField(primary_key=True)
    enc_algo = models.CharField(max_length=20) # -t ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa
    cert = models.TextField()
    owner_id = models.IntegerField()
    project_id = models.IntegerField() 


class SSHPrivateKey(models.Model):
    key_id =  models.ForeignKey(SSHPublicKey, on_delete=models.CASCADE)



# NVD(National Vulnerability Database)에 있는 보안 정보

class CveMain(models.Model):
    cve_id = models.CharField(max_length=20,unique=True)
    description = models.TextField()
    published_date = models.DateTimeField()
    last_modified = models.DateTimeField()
    source_id = models.CharField(max_length=50)

class CvssV3Metrics(models.Model):
    cve = models.ForeignKey(CveMain, on_delete=models.CASCADE, related_name='cvss_v3_metrics')
    base_score = models.DecimalField(max_digits=3, decimal_places=1)  # 7.5, 10.0 등
    base_severity = models.CharField(max_length=20)  # CRITICAL, HIGH, MEDIUM 등
    vector_string = models.CharField(max_length=150)
    exploitability_score = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    impact_score = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    # 분석 주체 (NVD, RedHat 등)
    source = models.CharField(max_length=100)
    type = models.CharField(max_length=50)  # Primary, Secondary 등


class AffectedProducts(models.Model):
    cve = models.ForeignKey(CveMain, on_delete=models.CASCADE, related_name='affected_products')
    # CPE 2.3 형식을 저장 (예: cpe:2.3:a:microsoft:word:2016:*:*:*:*:*:*:*)
    cpe_match = models.CharField(max_length=255)
    vulnerable = models.BooleanField()
    version_start_including = models.CharField(max_length=50, null=True, blank=True)
    version_end_excluding = models.CharField(max_length=50, null=True, blank=True)

class CveReferences(models.Model):
    cve = models.ForeignKey(CveMain, on_delete=models.CASCADE, related_name='references')
    url  = models.TextField()
    source  = models.CharField(max_length=100, null=True, blank=True)


class User(AbstractUser):
    display_name = models.CharField(max_length=50, blank=True, null=True)



