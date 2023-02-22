from pastebin_api import create_paste

title = "My Test Paste"
body = "Hello, World!"
expire = "10M"
public = True

url = create_paste(title, body, expire, public)
print(url)