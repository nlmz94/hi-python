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
                json_file_content += "\"" + member[0] + "\": \"" + member[1] + "\","
    json_file_content += '},}'
    json_file = open("generated_json.json", "wt")
    json_file.write(json_file_content)
    json_file.close()
