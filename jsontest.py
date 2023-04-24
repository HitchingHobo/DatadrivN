
import json

def dump_jsonl(data, output_path, append=False):
    """
    Write list of objects to a JSON lines file.
    """
    mode = 'a+' if append else 'w'
    with open(output_path, mode, encoding='utf-8') as f:
        for line in data:
            json_record = json.dumps(line, ensure_ascii=False)
            f.write(json_record + '\n')
    print('Wrote {} records to {}'.format(len(data), output_path))

def load_jsonl(input_path) -> list:
    """
    Read list of objects from a JSON lines file.
    """
    data = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.rstrip('\n|\r')))
    print('Loaded {} records from {}'.format(len(data), input_path))
    return data


data = load_jsonl('2022.sample.jsonl')

dist_list = []
x = 0


# def search(values, searchFor):
#     for k in values:
#         for v in values[k]:
#             if searchFor in v:
#                 return k
#     return None


## Data = list
## Data[0] = dict
## Data[0] innehåller tuples

values = data[0].values()
## print(values)
#print(type(values))


# Loop through list of dictionaries and search for "distans" in key description
for i in range(len(data)):
    for k in data[i].keys():
        for v in data[i][k]:
            if "distans" in v:
                dist_list.append(data[i])
                x += 1
                break
            else:
                break

print(dict_list)
print(x)

