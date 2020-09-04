import os

def handler(event, context):
    
    print os.environ.get('name')
    print("hello world")

    return "success"