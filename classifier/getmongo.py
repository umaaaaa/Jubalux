#usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient
import json

class convertMongo:
    con = MongoClient('172.16.4.84', 27017)
    db = con['sensordb']
    col = db.sensors
    global pre
    pre = db.predict
    global dic
    dic = {}
    count = 0

    for data in col.find():
        del data['_id']
# Bson$B$r(BJson$B$KJQ49(B
        json_list = json.dumps(data)
# Json$B$r%G%#%/%7%g%J%j$KJQ49(B
        dic[count] = json.loads(json_list)
        count += 1

    def getDic(self):
        return dic
    
    def postDB(self, result, value):
        pre.insert({'result':result, 'value':value})

    # count = 0
    # for count in dic:
    #     print dic[count]
