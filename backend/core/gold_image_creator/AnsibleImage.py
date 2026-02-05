import yaml

class VPSUsers:
    name

class PreInstalledDriver:
    

class AnsibleImage:
    image_name=""
    os_type=""
    ram_size=0
    cpu_count=0
    os_param=[]


    def generatePlaybook(self):

        data = self.image_name + " \n" +
                self.os_type + "\n" +
                self.ram_size + "\n" +
                self.cpu_count + "\n"
        
        with open('data.yaml', 'w') as f:
            yaml.safe_dump(data, f)


