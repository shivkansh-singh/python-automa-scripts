import requests 


file_url ="https://www.google.com/imgres?imgurl=https%3A%2F%2Fi0.wp.com%2Fnetworknuts.net%2Fwp-content%2Fuploads%2F2019%2F11%2Fnnlogosmall.png&tbnid=rX-07DwSpzGDsM&vet=12ahUKEwjo0JS1ndiDAxUfjmMGHYHvD6oQMygAegQIARBS..i&imgrefurl=https%3A%2F%2Fnetworknuts.net%2F&docid=pqFQ2MxH57rchM&w=451&h=451&q=images.google.com%20networknuts&ved=2ahUKEwjo0JS1ndiDAxUfjmMGHYHvD6oQMygAegQIARBS"

result = requests.get(file_url)


image = open("nn_logo.png","wb")

image.write(result.content)
image.close()
