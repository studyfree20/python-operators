#myarthmetic operators program code
#Introducing my signature libraries and functions
import hashlib
import base64
import urllib
'''
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
'''
#Arithmetic operators // addition
int1=4
int2=6
c=int1+int2
print(c)


#Arithmetic operators //floor
valuec = 17
valued = 6

print(valuec // valued)

#the floor division // rounds the result down to the nearest whole number

#Arithmetic operators // Exponentiation

x = 3
y = 3

print(x ** y) #same as 3*3*3

#Assignment operators

#substract add //It subtracts right operand from the left operand and assign the result to left operand
index1 = 10

index1 -= 4

print(index1)

#Divide add //It divides left operand with the right operand and assign the result to left operand

myval = 60

myval /= 7

print(myval)
# Comparison Operators

#Comparison Operators // equal
vala = 8070
valb = 600

# returns False because vala is not equal to valb
print(vala == valb)

# comparison operators // Less than or equal to
# returns False because 50 is neither less than or equal to 30
mark1 = 50
mark2 = 30

print(mark1 <= mark2)



#Logical Operators
#Logical Operators // AND Returns True if both statements are true

x = 999

print(x > 500 and x < 2000)

# comparison operators // not
#Reverse the result, returns False if the result is true
mynotval = 50

print(not(x > 45 and x < 100))

#Identity Operators
#Identity Operators // is not
myfruits = ["citrus", "berry"]
myfruitlist = ["citrus", "berry"]
myfruitss = myfruitlist
# returns true because they are silimar objects with similar contents
print(myfruits is not myfruitss)

# returns True because 
print(myfruitss is not myfruits)

# returns False because myfruts is equal to myfruitlist
print(myfruits != myfruitlist)

#Membership Operators
#Membership Operators not in

# returns True because a sequence with the value "benz" is not in the list
carlist = ["prado", "range rover"]

print("benz" not in carlist)

#Bitwise Operators
#Bitwise Operators
hexa1 = 0b1100
hexa2 = 0b1010
# and
print(bin(hexa1 & hexa2))

# or
print(bin(hexa1 | hexa2))
# xor
print(bin(hexa1 ^ hexa2))
# shift 2 bits left
print(bin(hexa1 << 2))
# shift 2 bits right
print(bin(hexa2 >> 2))
#end of all assignment oparators
class julius_api(object):
    def generate_signature(self, secret_key, http_method, request_path, query_params, request_body=''):
        signature = secret_key + http_method.upper() + request_path
        for key, value in query_params.iteritems():
            signature += key + '=' + value
        signature = base64.b64encode(hashlib.sha256(signature).digest())[0:43]
        signature = urllib.parse.quote(signature)
        return signature
