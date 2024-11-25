from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


class ChatApp(App):
    def build(self):
        self.root_layout = BoxLayout(orientation='vertical')

        #GORNY PASEK (Zostawiam na ikonki po analizie sentymentu)
        self.top_bar = BoxLayout(size_hint_y=None, height=200)
        with self.top_bar.canvas.before:
            Color(0.5, 0.5, 0.5, 1)
            self.rect = Rectangle(size=self.top_bar.size, pos=self.top_bar.pos)
        self.top_bar.bind(size=self._update_rect, pos=self._update_rect)
        self.root_layout.add_widget(self.top_bar)

        #OBSZAR CZATU
        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.messages_layout = GridLayout(cols=1, size_hint_y=None, spacing=10)
        self.messages_layout.bind(minimum_height=self.messages_layout.setter('height'))
        self.scroll_view.add_widget(self.messages_layout)
        self.root_layout.add_widget(self.scroll_view)

        #DOLNY PASEK, POLE TEKSTOWE I PRZYCISK
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
        message = self.text_input.text
        if message.strip():
            label = Label(text=message, size_hint_y=None, height=30, halign='left', valign='middle')
            label.text_size = (label.width, None)
            self.messages_layout.add_widget(label)


            self.text_input.text = ""

ChatApp().run()