from kivy.app import App
#kivy.require("1.9.1")
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.scrollview import ScrollView
from kivy.factory import Factory
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
import urllib
from urllib import urlencode



class MyLabelWithBackground(Label):
    pass

class ScreenManagement(ScreenManager):
    pass

class MyRow(BoxLayout):
    username = StringProperty('')
    

class MyButton(Button):
    text = StringProperty('username: ')
    username = StringProperty('')           

class SendmailScreen(Screen):
    invoice_number = StringProperty('')
    username = StringProperty('')
    purchase_order = StringProperty('')
    pass

    

class ItemScreen(Screen):
    invoice_number = StringProperty('')
    username = StringProperty('')
    purchase_order = StringProperty('')
    text = StringProperty('')
    pass
    
        
################################################   



class CreateinvoiceScreen(Screen):
    invoice_number = StringProperty('')
    username = StringProperty('')
    text = StringProperty('')
    suppliername = StringProperty('')
    pass
    
    

class LoggedScreen(Screen):
    suppliername = StringProperty('')
    username = StringProperty('')
    sessionid = StringProperty('')
    
    def back(self):
        print ("Going back")
        print (self.username)
        print(self.sessionid)
        self.manager.current = "start_screen"

    def error(self,username,password_in):
        print ("There was an error")
        self.manager.current = "error_screen"

    def fail(self,username,password_in):
        print ("Failed")
        self.manager.current = "fail_screen"


    def sessionid_validate(self, req, result):
        print ("jeah")     
        print(result)
        print (result["suppliername"])
        suppliername = result["suppliername"]
        print (suppliername)
        self.suppliername = str(result["suppliername"])
                     
        if str(result["status"]) == 'error':
            print("Error")
            
        else:
            print("Got Suppliername")
            
            self.manager.current = "createinvoice_screen"
        
    def createinvoice(self,sessionid):
        print ("Create invoice")
        print (self.sessionid)
        session_id = self.sessionid 
        print (session_id)
        
        print ("http-start")
        params = urllib.urlencode({'sessionid': sessionid})
        headers = {'Content-type': 'application/x-www-form-urlencoded',
                   'Accept': 'text/plain'}

        self.request = UrlRequest('https://www.myinv.org/api/getsupplierdata', req_body=params, req_headers=headers, on_success=self.sessionid_validate,
                                  on_failure=self.fail, on_error=self.error, method='POST', verify=False)

    
        

    

class SuccessScreen(Screen):
    pass

class ErrorScreen(Screen):
    pass

class FailScreen(Screen):
    pass

class StartScreen(Screen):
    username = StringProperty('')
    password_in = StringProperty('')
    wrong_cred = StringProperty('')
    text = StringProperty('')
    sessionid = StringProperty('')
    
    

    def error(self,username,password_in):
        print ("There was an error")
        self.manager.current = "error_screen"

    def fail(self,username,password_in):
        print ("Failed")
        self.manager.current = "fail_screen"


    def resetForm(self):
        self.ids['username'].text = ""
        self.ids['password'].text = ""
        self.wrong_cred = "Wrong credentials, try again"
        self.manager.current = "start_screen"

    def login_validate(self, req, result):
        try:          
            
            print("starting log_validate")
            print(result)
            # print(result["status"])
            print(self.username)
            self.sessionid = str(result["sessionid"])
            
            
            if str(result["status"]) == 'error':
                print("Wrong Credentials")
                self.resetForm()
            else:
                print("Password correct send to LoggedIn")
                self.text = self.username
                #print(result["sessionid"])
                #print (self.sessionid)
                self.manager.current = "logged_screen"
        except:
            print("Make sure both fields are filled")
            self.resetForm()
            
                

    def http_request_myinv_login(self,username, password_in):

        self.username = username
        self.password_in = password_in
        #print (username,password_in)
        #print ("http-start")
        params = urllib.urlencode({'username': username, 'password': password_in})
        headers = {'Content-type': 'application/x-www-form-urlencoded',
                   'Accept': 'text/plain'}

        self.request = UrlRequest('https://www.myinv.org/api/login', req_body=params, req_headers=headers, on_success=self.login_validate,
                                  on_failure=self.fail, on_error=self.error, method='POST', verify=False)
        #print(self.request)
        #print("Result: ", self.request.result)

    def __init__(self,**kwargs):
        super(StartScreen,self).__init__(**kwargs)


        def res(self, *args):
            print
            "Result: after success", self.request.result
########################################
























class MultiSelectSpinner(Button):
    background_color = 0, 1, 0, 1

    """Widget allowing to select multiple text options."""

    dropdown = ObjectProperty(None)
    """(internal) DropDown used with MultiSelectSpinner."""

    values = ListProperty([])
    """Values to choose from."""

    selected_values = ListProperty([])
    """List of values selected by the user."""

    def __init__(self, **kwargs):
        self.bind(dropdown=self.update_dropdown)
        self.bind(values=self.update_dropdown)
        super(MultiSelectSpinner, self).__init__(**kwargs)
        self.bind(on_release=self.toggle_dropdown)

    def toggle_dropdown(self, *args):
        if self.dropdown.parent:
            self.dropdown.dismiss()
        else:
            self.dropdown.open(self)

    def update_dropdown(self, *args):
        if not self.dropdown:
            self.dropdown = DropDown()
        values = self.values
        if values:
            if self.dropdown.children:
                self.dropdown.clear_widgets()
            for value in values:
                b = Factory.MultiSelectOption(text=value)
                b.bind(state=self.select_value)
                self.dropdown.add_widget(b)

    def select_value(self, instance, value):
        if value == 'down':
            if instance.text not in self.selected_values:
                self.selected_values.append(instance.text)
        else:
            if instance.text in self.selected_values:
                self.selected_values.remove(instance.text)

    def on_selected_values(self, instance, value):
        if value:
            self.text = ', '.join(value)
        else:
            self.text = ''

presentation = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    MainApp().run()


