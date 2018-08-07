# kivy_myinv_url
Login App POST request  
* Kivy version: 1.10.0  
* urllib3 version: 1.22  
  
  
The app built with kivy on Python 3.6 sends an HTTP POST REQUEST to www.myinv.org/login and processes the return.   

Now comes the odd part: Once I create the apk with buildozer (I'm using using the VM 17.04) the app crashes.  

On my local machine the app works. It fails at the following point: 
  
**main.kv**



    Button:
                color: 0,1,0,1
                text: 'Login'
                font_size: 30
                size: self.size
                on_press: root.http_request_myinv(login.text,password.text)
               
**main.py**  
  
  
    def http_request_myinv(self,username, password_in):

        self.username = username
        self.password_in = password_in
        print (username,password_in)
        print ("http-start")
        params = urllib.parse.urlencode({'username': 'mwell', 'password': password_in})
        headers = {'Content-type': 'application/x-www-form-urlencoded',
                   'Accept': 'text/plain'}

        self.request = UrlRequest('https://www.myinv.org/login', req_body=params,    req_headers=headers,on_success=self.login_validate)
        print(self.request)
        print("Result: ", self.request.result)  
          
            
            
        
 *Any idea why this goes wrong? Please see the files in the rep*
        

