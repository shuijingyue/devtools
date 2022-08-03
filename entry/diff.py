def read_change_logs(filename):
    result = {}
    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            if not line.startswith("Merge"):
                parts = line.split("|||")
                result[parts[0]] = {'subject': parts[0], 'owner': parts[1].strip()}
    return result

source = read_change_logs('source.log')
target = read_change_logs('target.log')
for key in source:
    if target.get(key) == None:
        print(source[key]['subject'], source[key]['owner'])
