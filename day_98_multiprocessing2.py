import multiprocessing
import requests

def downloadFile(url,name):
    respose=requests.get(url)
    open(f"files/file1{name}.jpg","wb").write(respose.content)
url="https://pixabay.com/vectors/list-icon-symbol-paper-sign-flat-2389219/"
for i in range(5):
    # downloadFile(url,i)
    p=multiprocessing.Process(target=downloadFile,args=[url,i])
    p.start()