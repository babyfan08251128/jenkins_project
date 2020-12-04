import yaml


def read_yaml(file_path,test_key):
    with open("./data/"+file_path,"r",encoding="utf_8") as f:
        data = yaml.load(f)
        #print(data)
        #for x in data.values():
        #    print(x)
        #传入scripts下模块名
        data_dict = data[test_key]
        #print(data_dict)
        list_data = []
        for i in data_dict.values():

            list_data.append(i)

        return list_data


