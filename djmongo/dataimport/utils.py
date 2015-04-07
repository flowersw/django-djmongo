#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

from django.conf import settings
from django.utils.datastructures import SortedDict
import os, json, sys, uuid, csv
from pymongo import Connection, DESCENDING
from bson.objectid import ObjectId
from pymongo import MongoClient


def bulk_csv_import_mongo(csvfile, database_name, collection_name, delete_collection_before_import=False):

    """return a response_dict  with a list of search results"""
    """method can be insert or update"""
    #print "writing ", csvfile._get_path(), "to the collection" , settings.MONGO_DB_NAME, settings.MONGO_MASTER_COLLECTION
    l=[]
    response_dict={}
    try:
        mconnection =   Connection(settings.MONGO_HOST, settings.MONGO_PORT)
        db = 	        mconnection[database_name]

        collection = db[collection_name]
        
        if delete_collection_before_import:
            myobjectid=collection.remove({})
            
        #open the csv file.
        csvhandle = csv.reader(open(csvfile._get_path(), 'rb'), delimiter=',')
        
        rowindex = 0
        errors=0
        error_list =[]
        success =0
        for row in csvhandle :
            
            if rowindex==0:
                 column_headers = row
                 cleaned_headers = []
                 for c in column_headers:
                    c= c.replace(".", "")
                    c =c.replace("$", "-")
                    c =c.replace(" ", "_")
                    cleaned_headers.append(c)
            else:
          
                record = dict(zip(cleaned_headers, row))
                #if there is no values, skip the key value pair
                kwargs ={}
        
                #Only populate fields that are not blank.
                for k,v in record.items():
                    if v:
                        if v.isdigit():
                            kwargs[k]=int(v)
                        else:
                            kwargs[k]=v
                        
                try:
                    
                    myobjectid=collection.insert(kwargs)
                    success+=1
                except:
                    error_message = "Error on row " + rowindex +  ". " + str(sys.exc_info())
                    error_list.append(str(sys.exc_info()))
                
  
            rowindex+=1
            
        if error_list:
            response_dict ={}
            response_dict['num_rows_imported']=rowindex
            response_dict['num_rows_errors']=len(error_list)
            response_dict['errors']=error_list
            response_dict['code']=400
            response_dict['message']="Completed with errors"
        else:
            
            response_dict ={}
            response_dict['num_rows_imported']=success
            response_dict['code']=200
            response_dict['message']="Completed."
        return response_dict  
        
    
            
    except:
        #print "Error reading from Mongo"
        #print str(sys.exc_info())
        response_dict['num_results']=0
        response_dict['code']=400
        response_dict['type']="Error"
        response_dict['results']=[]
        response_dict['message']=str(sys.exc_info())
    return response_dict
