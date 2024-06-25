def handler(event, context):
    print("Hello from Lambda1!")
    print("Hello from Lambda1!")
    print("Hello from Lambda1!")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda1!-change')
    }