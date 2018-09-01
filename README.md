# kivy_myinv_url
e-invoice creation app in conjunction with www.myinv.org/api  
* Kivy version: 1.10.0  
* urllib3 version: 1.22  
  
  
The app built with kivy on Python 2.7 sends an HTTP POST REQUEST to www.myinv.org/api/login and processes the return.

If the credentials are correct, the user is logged in. Get your account under www.myinv.org/signup/ 

For deployment I use the Ubuntu **17.04** virtual machine provided on the kivy page. When deploying in the build directory the following commands are used:

    buildozer android clean  
    buildozer android debug deploy run 



   
       
   
   
        

