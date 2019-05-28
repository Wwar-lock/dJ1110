from django.shortcuts import render  
# render the views
import pyrebase

config = {
  'apiKey': "AIzaSyCP19AOvCDxB5ADdxsEFKBQYb_6-bqg8F8",
  'authDomain': "dj1110.firebaseapp.com",
  'databaseURL': "https://dj1110.firebaseio.com",
  'projectId': "dj1110",
  'storageBucket': "dj1110.appspot.com",
  'messagingSenderId': "663631638107",
  'appId': "1:663631638107:web:73e3ffe8432075cc"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def signIn(request):
    return render(request,"signIn.html")
    # just simply render the page












# <!-- The core Firebase JS SDK is always required and must be listed first -->
# <script src="/__/firebase/6.0.4/firebase-app.js"></script>

# <!-- TODO: Add SDKs for Firebase products that you want to use
#      https://firebase.google.com/docs/web/setup#reserved-urls -->

# <!-- Initialize Firebase -->
# <script src="/__/firebase/init.js"></script>