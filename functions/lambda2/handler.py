def handler(event, context):
    print("Hello from Lambda2!")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda2!')
    }