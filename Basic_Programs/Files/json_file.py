import json
with open("./data.json","r",encoding="utf-8") as d:
    data = json.load(d)
print(data)

new_data = data
new_data['local']['uvm_count'] = 44
print(data)
json.dump(new_data, open("./data.json","w"), ensure_ascii=False)
