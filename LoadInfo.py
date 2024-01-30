import xml.etree.ElementTree as ET

class LoadInfo:
    def __init__(self):
        pass
    
    def loadFromXml(xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        data = {}

        for line in root.findall('line'):
            line_name = line.get('name')
            data[line_name] = {}

            for machine_type in line.findall('machineType'):
                machine_type_name = machine_type.get('name')
                data[line_name][machine_type_name] = {}

                for machine in machine_type.findall('machine'):
                    machine_name = machine.get('name')
                    host_info = machine.find('host')
                    if host_info is not None:
                        host_name = host_info.get('name')
                        host_pwd = host_info.get('pwd')
                        host_id = host_info.get('id')
                        data[line_name][machine_type_name][machine_name] = [host_name, host_pwd, host_id]

        return data