import json
with open("E:/uniprotkb_AND_reviewed_true_2023_09_15.json",'r') as src:
    data_src=json.load(src)
    print("open source")
    with open("E:/result.json",'w') as target:
        print("opened target")
        data_selected=list()
        for i in data_src["results"]:
            seq=i["sequence"]["value"]
            if "ecNumbers" in i["proteinDescription"]["recommendedName"]:
                tag=int(i["proteinDescription"]["recommendedName"]["ecnumbers"]["value"][0])
            else:
                tag=0
            print(seq,tag)
            data_selected.append({"seq":seq,"tag":tag})
        json.dump(data_selected,target)
