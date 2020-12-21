from urllib import parse
import base64
import binascii
import binhex


def Base64Decode():
    test = input("Enter base64 -> ")
    data_encoded = base64.b64decode(test)
    data_encoded = base64.urlsafe_b64decode(test)
    print ("\n--------------------------")
    print(data_encoded.decode())
    print ("\n--------------------------")
    input("Press Enter to exit")

def Base64Encode():
    test = input("Enter text to Encode ")
    data = base64.b64encode(test.encode())
    print ("\n-------------------------")
    print(data.decode())
    print ("\n-------------------------")
    input ("Press Enter to exit")


def UrlDecode(string):
    test = input("Enter Encoded URL ->")
    try:
        protocol = string[:string.index("//")]+ "//"
    except ValueError:
        protocol = "http://"
    string = string.replace("http://","", 1)
    string = string.replace("https://","", 1)
    if "/" in string:
        string = parse.unquote(string.replace(string[:string.index("/")], bytearray(string[:string.index("/")],"idna").decode("idna"),1),encoding='utf-8')
    else:
        string = bytearray(string, "idna").decode("idna")
    print ("\n--------------------------")
    string= protocol + string
    print (string)
    print ("\n--------------------------")
    input ("Press Enter to exit")


choice = input("Enter\n -Base64Decode:1 \n -Base64Encode:2 \n -URLDecoder:3 \n")

if choice == "1":
    Base64Decode()
if choice == "2":
    Base64Encode()
if choice == "3":
    UrlDecode()
else : 
    print("Done")
