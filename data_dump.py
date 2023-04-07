import pymongo
import pandas as pd
import json

from sensor.config import mongo_client

Data_File_Path = "/config/workspace/aps_failure_training_set1.csv"
Database_Name = "aps"
Collection_Name = "sensor"

if __name__=="__main__":
    df = pd.read_csv = (Data_File_Path)
    print(f"Rows and columns : {df.shape}")
    
    # convert dataframe to json so that we can dump these records to mongodb
    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    print (json_record[0])

    #insert converted json record to mongo_db
    mongo_client[Database_Name][Collection_Name].insert_many(json_record)
    