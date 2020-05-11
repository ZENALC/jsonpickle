# issue number 275
# encoding the lambda function
# Marie Clancy
# file number 3

import jsonpickle

# filename
filename = "functionLambda.json"

# load filename in read mode
with open(filename, "r") as n:
    # variable "read" is now equal to n.read()
    read = n.read()
    # decoding function... decode what we just read
    lambdaExpression1 = jsonpickle.decode(read, encodeFunctionItself=True)
    # execute the code
    exec(lambdaExpression1)
print(lambdaExpression1(5))
