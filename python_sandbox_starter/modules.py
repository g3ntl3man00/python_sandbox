# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules


# core modules 

from time import time
timestamp = time()

print (timestamp) 
# pip module
import camelcase
# Custom modules 

from validator import validate_email

camel = camelcase.CamelCase()
text= 'hello there everyone'
print(camel.hump(text))

email = 'test@test.com'
if validate_email(email):
 print('email is valid') 
else:
 print ('email is not valid')    


