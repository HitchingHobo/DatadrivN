

# def dump_jsonl(data, output_path, append=False):
#     """
#     Write list of objects to a JSON lines file.
#     """
#     mode = 'a+' if append else 'w'
#     with open(output_path, mode, encoding='utf-8') as f:
#         for line in data:
#             json_record = json.dumps(line, ensure_ascii=False)
#             f.write(json_record + '\n')
#     print('Wrote {} records to {}'.format(len(data), output_path))

# def load_jsonl(input_path) -> list:
#     """
#     Read list of objects from a JSON lines file.
#     """
#     data = []
#     with open(input_path, 'r', encoding='utf-8') as f:
#         for line in f:
#             data.append(json.loads(line.rstrip('\n|\r')))
#     print('Loaded {} records from {}'.format(len(data), input_path))
#     return data


# data = load_jsonl('2022.sample.jsonl')

# dist_list = []
# x = 0


# ## Data = list
# ## Data[0] = dict
# ## Data[0] innehåller tuples



# values = data[0].keys()



import json
import pandas as pd


# with open('2022.sample.jsonl', encoding=('UTF8')) as f:
#     lines = f.read().splitlines()

# df_inter = pd.DataFrame(lines)
# df_inter.columns = ['json_element']

# df_inter['json_element'].apply(json.loads)

# df_final = pd.json_normalize(df_inter['json_element'].apply(json.loads))
# print(df_final.head(2))


lines = []
with open(r'2022.sample.jsonl', encoding=('UTF8')) as f:
    lines = f.read().splitlines()

line_dicts = [json.loads(line) for line in lines]
df_final = pd.DataFrame(line_dicts)

print(df_final)