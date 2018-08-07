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


class MyLabelWithBackground(Label):
    pass
class ScreenManagement(ScreenManager):
    pass

class LoggedScreen(Screen):
    pass



class StartScreen(Screen):
    username = StringProperty('')
    password_in = StringProperty('')
    wrong_cred = StringProperty('')

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""
        #self.wrong_cred = "Wrong credentials, try again"
        self.manager.current = "start_screen"

    def login_validate(self, req, result):
        print("starting log_val")
        print(result)
        # print(result["status"])

        if str(result["status"]) == 'error':
            print("Switch to some class/screen")
            self.resetForm()

        else:
            print("Password correct send to LoggedIn")
            self.manager.current = "logged_screen"

    def http_request_myinv(self,username, password_in):

        self.username = username
        self.password_in = password_in
        print (username,password_in)
        print ("http-start")
        params = urllib.parse.urlencode({'username': 'mwell', 'password': password_in})
        headers = {'Content-type': 'application/x-www-form-urlencoded',
                   'Accept': 'text/plain'}

        self.request = UrlRequest('https://www.myinv.org/login', req_body=params, req_headers=headers,on_success=self.login_validate)
        print(self.request)
        print("Result: ", self.request.result)


    def __init__(self,**kwargs):
        super(StartScreen,self).__init__(**kwargs)






        def res(self, *args):
            print
            "Result: after success", self.request.result

























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


