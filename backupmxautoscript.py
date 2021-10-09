# @author:Prajith Ramachandran
# function to backup and version Maximo automation script 
import json
import boto3
import xml.etree.ElementTree as ET
#Automation script xml on request body
def lambda_handler(event, context):
    reqbody=event['body']
    #print(reqbody)
    filebytes = reqbody
    encoded_filebytes = filebytes.encode("utf-8")
    bucket_name = "prajith"
    file_name = parseXMLToGetScriptNName(reqbody)
    s3_path = "mxauoscripts/" + file_name
    s3 = boto3.resource("s3")
    s3.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_filebytes)

    print("Backing up of Script :"+bucket_name+"/"+s3_path+" is sucessful.")
    return createresponse("Backing up of Script :"+bucket_name+"/"+s3_path+" is sucessful.",200)
    
def createresponse(message,status_code):
    return {
        'statusCode': str(status_code),
        'body': json.dumps(message),
        'headers': {
            "Content-Type":"application/json",
            "Access-Control-Allow-Origin":"*",
            "Access-Control-Allow-Methods":"OPTIONS,POST,GET"
            },
}
#get ScriptName from XML
def parseXMLToGetScriptNName(mxxml):
   print("starting parse 2....")
   root = ET.fromstring(mxxml)
   print(root)
   for child1 in root:
       print(child1)
       for child2 in child1:
           return (child2[2].text+".xml")
  
  
