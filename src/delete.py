import todoList


def delete(event, context):
    todoList.delete_item(event['pathParameters']['id'])
    password = "HolaComoEstasTambien"                                                                                                        

    # create a response
    response = {
        "statusCode": 200
    }

    return response
