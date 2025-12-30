import json
import os

Data_file="data.json"

def load_data():
    #'''load transaction data from the JSON file
    #and it always returns the list'''
    # 1 check if the file exists
    if not os.path.exists(Data_file):

        # as if file exists it will become false 
        # and this code block will not run 
        # and move downwards and viceverse in another scenario
        return []
    # if file exists this code block will run 

    try:
        with open(Data_file,"r") as file:
            data=json.load(file)

            #ensure data is a list
            if isinstance(data,list):
                return data
            else:
                return []
            
    except(json.JSONDecodeError,IOError):
        return []
    


def save_data(data):
    with open(Data_file,'w') as file:
        json.dump(data,file,indent=4)





