from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image


user_message = ""
fear_perc = 0
luck_perc = 0

class ChatApp(App):
    def build(self):
        self.root_layout = BoxLayout(orientation='vertical')

        # GÓRNY PASEK (z ikonami)
        self.top_bar = BoxLayout(size_hint_y=None, height=200, padding=10, spacing=10)
        with self.top_bar.canvas.before:
            Color(0.5, 0.5, 0.5, 1)  # Tło szare
            self.rect = Rectangle(size=self.top_bar.size, pos=self.top_bar.pos)
        self.top_bar.bind(size=self._update_rect, pos=self._update_rect)

        # IKONKI
        happy_icon = Image(source='luck.png', size_hint=(None, None), size=(80, 80), pos_hint={"center_y": 0.5})
        spacer = Widget(size_hint=(1, 1)) 
        fear_icon = Image(source='fear.png', size_hint=(None, None), size=(80, 80), pos_hint={"center_y": 0.5})

        # Wyswietlenie emotki szczescia wraz z wartoscia procentowa (czy cokolwiek co bedziemy uzywac)
        # Etykieta dla szczęścia
        happy_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(80, 120))
        happy_layout.add_widget(happy_icon)
        self.happy_label = Label(text=f"{luck_perc}%", size_hint=(1, None), height=20, halign='center')
        self.happy_label.text_size = (self.happy_label.width, None)
        happy_layout.add_widget(self.happy_label)
        self.top_bar.add_widget(happy_layout)

        #Spacer
        self.top_bar.add_widget(spacer)

        #Strach
        fear_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(80, 120))
        fear_layout.add_widget(fear_icon)
        self.fear_label = Label(text=f"{fear_perc}%", size_hint=(1, None), height=20, halign='center')
        self.fear_label.text_size = (self.fear_label.width, None)
        fear_layout.add_widget(self.fear_label)
        self.top_bar.add_widget(fear_layout)

        self.root_layout.add_widget(self.top_bar)

        # OBSZAR CZATU
        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.messages_layout = GridLayout(cols=1, size_hint_y=None, spacing=10)
        self.messages_layout.bind(minimum_height=self.messages_layout.setter('height'))
        self.scroll_view.add_widget(self.messages_layout)
        self.root_layout.add_widget(self.scroll_view)

        # DOLNY PASEK, POLE TEKSTOWE I PRZYCISK
        self.bottom_bar = BoxLayout(size_hint_y=None, height=50)
        self.text_input = TextInput(hint_text="Opisz swój sen...", multiline=False)
        self.text_input.bind(on_text_validate=self.submit_text)
        self.submit_button = Button(text="Wyślij")
        self.submit_button.bind(on_press=self.submit_text)

        self.bottom_bar.add_widget(self.text_input)
        self.bottom_bar.add_widget(self.submit_button)
        self.root_layout.add_widget(self.bottom_bar)

        return self.root_layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def submit_text(self, instance):
        user_message = self.text_input.text
        if user_message.strip():
            # WIADOMOŚĆ USERA
            user_label = Label(text=user_message, size_hint_y=None, height=30, halign='left', valign='middle')
            user_label.text_size = (user_label.width, None)
            self.messages_layout.add_widget(user_label)

            # BOT ODPOWIADA
            bot_label = Label(text="Siema", size_hint_y=None, height=30, halign='left', valign='middle')
            bot_label.text_size = (bot_label.width, None)
            self.messages_layout.add_widget(bot_label)

            self.text_input.text = ""

        
    def update_percentages(self, fear, luck):
        self.fear_label.text = f"{fear}%"
        self.happy_label.text = f"{luck}%"

ChatApp().run()