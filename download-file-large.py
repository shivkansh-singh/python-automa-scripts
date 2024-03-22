import requests

file_url = "https://files.testfile.org/PDF/40MB-TESTFILE.ORG.pdf"

result = requests.get(file_url,stream=True)


with open("data.pdf","wb") as mypdf:
        for data in result.iter_content(chunk_size=1024):
            if data:
                mypdf.write(data)



#image = open("nn_logo.png","wb")
#image.write(result.content)
#image.close()



