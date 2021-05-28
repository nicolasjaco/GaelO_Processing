

def abstract():
    return

def post_process():
    result = stub.Predict(grpc_request,10)
    print(result)
    resultDict = {}
    for output in result.outputs:
        outputResult = result.outputs[output]
        resultDict[str(output)] = list(outputResult.float_val)
    return resultDict
