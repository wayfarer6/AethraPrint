from django.db import models

# Create your models here.


class node(models.Model):
    node_name = models.CharField(max_length=50)
    node_ip = models.CharField(max_length=30)
    node_auth = models.CharField(max_length=10) # ssh, 등등 연결 방식

    def edit_ip(new_ip):
        node_ip = new_ip