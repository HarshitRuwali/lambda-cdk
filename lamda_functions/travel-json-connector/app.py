import json
def lambda_handler(event, context):
    print("data from request hub : ", event)

    print("Hello from JSON connector -- sdeplkj 45433")
    return {
        "statusCode": 200,
        "body": json.dumps("Hello from JSON connector -- sdeplkj 45433")
    }
# import json
# def lambda_handler(event, context):
#     request = json.loads(event['body'])
#     resp = {
#         "output": request['url']
#     }
#     return {
#         "statusCode": 200,
#         "headers": {},
#         "body": json.dumps(resp)
#     }