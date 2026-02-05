# Back with Virtualbox
import os
from core.models import VPSImage, OSParam, VPSUser
from datetime import datetime
from jinja2 import Environment, FileSystemLoader


PROVIDER_TEMPLATES = {
    "virtualbox-iso": "packer_template_for_virtualbox-iso.j2",
    "aws": "packer_template_for_aws.j2",
    "azure": "packer_template_for_azure.j2"
}

# os_type 별 boot command 

## vhd stroage design 시 필요한 커맨드는 나중에 리펙토링하기...
## 지금으로서는 자동으로 전체 파티션 잡는걸로 

# ubuntu 

ubuntu_cmd = [
    "<esc><wait>",
    "linux /casper/vmlinuz quiet autoinstall ds=nocloud-net; s=http://{{ .HTTPIP }}:{{ .HTTPPort }}/ <enter>",
    "initrd /casper/initrd<enter>",
    "boot<enter>"
]
 # 실제로 packer가 직접 엔터를 처가면서 입력하는 거임

# debian

debian_cmd = [
    "<esc><wait>",
    "linux /casper/vmlinuz quiet autoinstall ds=nocloud-net; s=http://{{ .HTTPIP }}:{{ .HTTPPort }}/ <enter>",
    "initrd /casper/initrd<enter>",
    "boot<enter>"
]

#Based on Kickstart

## Redhat

redhat_cmd = [
    "<esc><wait>",
    "append initrd=initrd.img inst.ks=http://{{ .HTTPIP }}:{{ .HTTPPort }}/ks.cfg <enter>",
    "boot<enter>"
]


## Rocky

rocky_cmd = [
    "<esc><wait>",
    "append initrd=initrd.img inst.ks=http://{{ .HTTPIP }}:{{ .HTTPPort }}/ks.cfg <enter>",
    "boot<enter>"
]

OS_COMMAND ={
    "redhat":redhat_cmd,
    "rocky": rocky_cmd,
    "ubuntu":ubuntu_cmd,
    "debian":debian_cmd,
}

ISO_IMAGE= {

}

ISO_CHECKSUM= {
    
}

#filename는 별도 설정 하거나 자동 생성하기 (일단 자동생성)

### 일단 provider는 virtualbox 고정, 추후에 vmware, aws 등등 추가 예정~~~

def packer_hcl_creator(project_name,project,path,VPSImage,provider):
    time_stamp = datetime.now()
    filename = f"{project_name}_{VPSImage.vps_name}_{time_stamp.strftime('%Y%m%d_%H%M%S')}.pkr.hcl"
    
    image_full_path = os.path.join(project_path,"Image","Packer",filename)
    file_full_path = os.path.join(project_path,filename)
    

    template_dir = os.path.join(os.getcwd(),'templates')
    env = Environment(loader=FileSystemLoader(template_dir))
    tpl_name = PROVIDER_TEMPLATES.get(provider.lower()) # 혹시나 대문자로 호출 할때 대비
    
    template = env.get_template(tpl_name)
    os_key = VPSImage.os_type.lower()
    rendered_hcl = template.render(
            vm_name=f"{VPSImage.vps_name}-Packer-{time_stamp}-time",
            guest_os_type=os_key,
            iso_url=
            iso_checksum=
            cpus=VPSImage.cpu_cnt
            memory=VPSImage.ram_size
            disk_size=VPSImage.disk_size
            iso_interface=sata #추후 인자로 받을 수 있도록 수정
            boot_commands=OS_COMMAND.get(os_key)
            ssh_password=
    )
    with open(filename, 'w') as f:
        f.write(rendered_hcl)


    return file_full_path
