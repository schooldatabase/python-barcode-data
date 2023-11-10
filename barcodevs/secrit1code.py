import secrets 

url = 'https://database.com/index=' + secrets.token_urlsafe() 
print(url) 