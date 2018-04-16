import urllib.request
from firebase import firebase

firebase = firebase.FirebaseApplication('https://plant-wahid.firebaseio.com/plant-wahid')


res = firebase.get('/',None)
print(res['author'])
if(res['author'] == 'clientside'):
    urllib.request.urlretrieve(res['imageString'], "local-filename.jpg")
