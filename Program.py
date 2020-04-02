import urllib.request

def read_text():
    quotes = open("file.txt","r")    
    contents = quotes.read()
    print(contents)    
    quotes.close()
    return contents
    
def check_content_profanity(text_to_check):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check) 
    output = connection.read()
    print(output)
    connection.close()

    if ('true'):
        print ("There is profanity in this document.")
    else:
        print ("No profanity found in this document.")
if __name__ == "__main__":
    contents = read_text()
    check_content_profanity(contents)
    