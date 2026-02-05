import os

def init_project(root_dir,project_name):
    
    project_path = os.path.join(root_dir,project_name)

    os.makedirs(project_path, exist_ok=True)

    file_list = [
        "blueprint.cf",
        "blueprint_db.sqlite3",
        "vps_data.json",
        "opentufu_data.json",
        "namespace_config.json",
        "pod.json",
        "subnet.json",
        "firewall.json",
        "namespace_network.json",
        "vps_network_config.json",
        "vps_package.json",
        "kern_param.json",
        "security_test_result.json"
    ]

    for filename in file_list:
        file_full_path = os.path.join(project_path,filename)

        with open(file_full_path,'w',encoding='utf-8') as f:
            pass # create blank file
        