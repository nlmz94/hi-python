import re


def ini_to_json(file_string):
    json_file_content = '{'
    for line in file_string.split("\n"):
        if re.match(r'^\[.*]$', line.strip()) and line.strip():
            group = line.strip('[').strip(']')
            json_file_content += "\"" + group + "\": {"
        elif not line.strip() or line in ['\n', '\r\n']:
            json_file_content += "},"
        else:
            if not re.match(r'^#.*', line) and line.strip():
                member = line.replace(' = ', ': ').split()
                json_file_content += "\"" + \
                    member[0] + "\": \"" + member[1] + "\","
    json_file_content += '},}'
    json_file = open("generated_json.json", "wt")
    json_file.write(json_file_content)
    json_file.close()


def json_to_ini(json_data):
    ini_file_content = ""
    for key in json_data.keys():
        ini_file_content += "[" + key + "]\n"
        for sub_key in json_data[key].keys():
            ini_file_content += sub_key + "=" + json_data[key][sub_key] + "\n"
        ini_file_content += "\n"
    ini_file = open("generated_ini.ini", "wt")
    ini_file.write(ini_file_content)
    ini_file.close()
