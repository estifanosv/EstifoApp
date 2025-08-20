
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import datetime

# Simulated user database
users = {}
trial_start = {}

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.username = TextInput(hint_text='Username', multiline=False)
        self.password = TextInput(hint_text='Password', multiline=False, password=True)
        login_btn = Button(text='Login')
        login_btn.bind(on_press=self.login)
        register_btn = Button(text='Register')
        register_btn.bind(on_press=self.register)
        layout.add_widget(Label(text='Login'))
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(login_btn)
        layout.add_widget(register_btn)
        self.add_widget(layout)

    def login(self, instance):
        uname = self.username.text
        pwd = self.password.text
        if uname in users and users[uname] == pwd:
            self.manager.current = 'home'
        else:
            self.manager.current = 'login'

    def register(self, instance):
        uname = self.username.text
        pwd = self.password.text
        if uname not in users:
            users[uname] = pwd
            trial_start[uname] = datetime.datetime.now()
            self.manager.current = 'home'

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Welcome to the Book App'))
        read_btn = Button(text='Read Book')
        read_btn.bind(on_press=self.read_book)
        audio_btn = Button(text='Play Audio')
        audio_btn.bind(on_press=self.play_audio)
        qa_btn = Button(text='Q&A Section')
        qa_btn.bind(on_press=self.qa_section)
        pay_btn = Button(text='Payment')
        pay_btn.bind(on_press=self.payment)
        layout.add_widget(read_btn)
        layout.add_widget(audio_btn)
        layout.add_widget(qa_btn)
        layout.add_widget(pay_btn)
        self.add_widget(layout)

    def read_book(self, instance):
        self.manager.current = 'book'

    def play_audio(self, instance):
        self.manager.current = 'audio'

    def qa_section(self, instance):
        self.manager.current = 'qa'

    def payment(self, instance):
        self.manager.current = 'payment'

class BookScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        try:
            with open('assets/book.txt', 'r') as f:
                content = f.read()
        except:
            content = "Book content not found."
        layout.add_widget(Label(text=content))
        back_btn = Button(text='Back')
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'home'

class AudioScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Audio playback placeholder'))
        back_btn = Button(text='Back')
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'home'

class QAScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Q&A Section'))
        layout.add_widget(Label(text='Question: What is the book about?'))
        layout.add_widget(Label(text='Answer: This is a sample book.'))
        back_btn = Button(text='Back')
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'home'

class PaymentScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Payment Required'))
        layout.add_widget(Label(text='Please proceed to payment after trial.'))
        back_btn = Button(text='Back')
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'home'

class BookApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(BookScreen(name='book'))
        sm.add_widget(AudioScreen(name='audio'))
        sm.add_widget(QAScreen(name='qa'))
        sm.add_widget(PaymentScreen(name='payment'))
        return sm

if __name__ == '__main__':
    BookApp().run()
