#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Last modified on Thursday June 16 19:11 2022

@author: oscarpiette
"""


from fastapi import FastAPI, Request, File, UploadFile
import aiofiles
from pydantic import BaseModel
import morph_kgc
import json
import sys
import os


app=FastAPI()


@app.post("/files/")
async def upload_file(file: UploadFile):
    
    try:
        input_file = await file.read()
        input_file = input_file.decode('utf8')
        input_json = json.loads(input_file)
        
        if "paper" not in input_json:
            return 'KeyError: "paper" expected, try creating a json with "paper" as a key and the paper json as the value'
        
        if "paragraph" not in input_json:
            return 'KeyError: "paragraph" expected, try creating a json with "paragraph" as a key and the paper json as the value'
       
        
        config="[DataSourceJSON]\nmappings=semantificator_API/mapping.ttl"
        
        with open('semantificator_API/solr-paper.json', 'w') as openfile:
            json.dump(input_json["paper"], openfile)
        
        with open('semantificator_API/solr-evidences.json', 'w') as openfile:
            json.dump(input_json["paragraph"], openfile)
            
        graph = morph_kgc.materialize(config)

        graph.serialize(destination="semantificator_API/kg.ttl", format="ttl", encoding="utf-8")
        with open("semantificator_API/kg.ttl", 'r') as openfile:
            KG = openfile.readlines()
            KG = "".join(KG)
        return({"KG":KG})
 
    except Exception:
        return {"Error": Exception}
    