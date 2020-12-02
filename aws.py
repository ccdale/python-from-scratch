import boto3


sess = boto3.session.Session(profile_name="sdev")
ddb = sess.client("dynamodb")

tablename = "AWSAccountAdmin"

items = ddb.scan(TableName=tablename)


# TODO:
# retrieve all items from table
# decode the item into python form
# search for the item required from the command line
# make generic to allow searching any table in any profile

for item in items["Items"]:
    print(item)
    break


"""
{
'Reservations': [],
'ResponseMetadata': {'RequestId': '766ff0cd-4672-4d8d-94c3-45259733859a',
'HTTPStatusCode': 200,
'HTTPHeaders': {'x-amzn-requestid': '766ff0cd-4672-4d8d-94c3-45259733859a',
'content-type': 'text/xml;charset=UTF-8',
'content-length': '230',
'date': 'Wed,
02 Dec 2020 15:19:11 GMT',
'server': 'AmazonEC2'},
'RetryAttempts': 0}}
"""
