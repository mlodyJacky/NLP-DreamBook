import json
import os
from functools import partial
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.image import Image


class ChatApp(App):
    DATA_FILE = "chat_logs.json"

    def build(self):
        self.root_layout = BoxLayout(orientation='horizontal')
        self.chat_logs = []
        self._load_chats_from_file()
        self._create_left_panel()
        self._create_right_panel()
        return self.root_layout
    
    def on_start(self):
        self.title = "DreamMate"

    def _create_left_panel(self):
        self.left_layout = BoxLayout(size_hint=(0.2, 1))
        self._add_background(self.left_layout, (0.278, 0.250, 0.455, 1))
        self.left_scroll = ScrollView(size_hint=(1, 1))
        self.left_grid = GridLayout(cols=1, size_hint_y=None, spacing=10, padding=10)
        self.left_grid.bind(minimum_height=self.left_grid.setter('height'))
        self.left_scroll.add_widget(self.left_grid)
        self.left_layout.add_widget(self.left_scroll)
        self.root_layout.add_widget(self.left_layout)

        self._populate_journal_entries()

    def _create_right_panel(self):
        self.right_layout = BoxLayout(orientation='vertical', size_hint=(0.8, 1))
        self._create_top_bar()
        self._create_chat_area()
        self._create_bottom_bar()
        self.root_layout.add_widget(self.right_layout)

    def _create_top_bar(self):
        self.top_bar = BoxLayout(
            size_hint_y=None, 
            height=200, 
            padding=[10, 10, 20, 10], 
            spacing=10, 
            orientation='horizontal',
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self._add_background(self.top_bar, (0.278, 0.250, 0.455, 1))

        central_layout = BoxLayout(
            orientation='horizontal',
            size_hint=(None, None),
            spacing=15
        )

        emotions = [
            ("resources/happiness.png", "0%"),
            ("resources/sadness.png", "0%"),
            ("resources/anger.png", "0%"),
            ("resources/fear.png", "0%"),
        ]

        for icon, percentage in emotions:
            self._create_emotion_widget(icon, percentage, central_layout)

        self.new_button = Button(
            text="Start fresh",
            size_hint=(None, None),
            size=(120, 60),
            background_color=(0.278, 0.250, 0.455, 1),
            color=(1, 1, 1, 1),
            font_name='resources/poppins.ttf',
        )
        self.new_button.bind(on_press=self.start_new_chat)
        central_layout.add_widget(self.new_button)

        self.top_bar.add_widget(Widget(size_hint=(0.3, 1)))
        self.top_bar.add_widget(central_layout)
        self.top_bar.add_widget(Widget(size_hint=(1, 1)))

        self.right_layout.add_widget(self.top_bar)

    def _create_emotion_widget(self, icon_source, percentage, parent_layout):
        layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(80, 120))
        icon = Image(source=icon_source, size_hint=(None, None), size=(70, 70), pos_hint={"center_y": 0.5})
        label = Label(text=percentage, size_hint=(1, None), height=20, halign='center')
        label.text_size = (label.width, None)
        layout.add_widget(icon)
        layout.add_widget(label)
        parent_layout.add_widget(layout)


    def _create_chat_area(self):
        self.scroll_view = ScrollView(size_hint=(1, 1))
        self._add_background(self.scroll_view, (0.378, 0.350, 0.555, 1))

        self.messages_layout = GridLayout(cols=1, size_hint_y=None, spacing=10)
        self.messages_layout.bind(minimum_height=self.messages_layout.setter('height'))
        self.scroll_view.add_widget(self.messages_layout)
        self.right_layout.add_widget(self.scroll_view)

    def _create_bottom_bar(self):
        self.bottom_bar = BoxLayout(size_hint_y=None, height=90)

        self.text_input = TextInput(
            hint_text="Describe your dream and well-being...",
            multiline=True,
            foreground_color=(0, 0, 0, 1),
            background_color=(0.9, 0.9, 0.9, 1),
            font_size=16,
            padding=[10, 10],
            font_name='resources/poppins.ttf',
        )
        self.text_input.background_normal = ''
        self.text_input.background_active = ''

        self.send_button = Button(text="Send", background_color=(0.278, 0.250, 0.455, 1), color=(1, 1, 1, 1), font_name='resources/poppins.ttf')
        self.send_button.bind(on_press=self.submit_text)

        self.save_button = Button(text="Save", background_color=(0.378, 0.350, 0.555, 1), color=(1, 1, 1, 1), font_name='resources/poppins.ttf')
        self.save_button.bind(on_press=self.save_chat)

        self.bottom_bar.add_widget(self.text_input)
        self.bottom_bar.add_widget(self.send_button)
        self.bottom_bar.add_widget(self.save_button)
        self.right_layout.add_widget(self.bottom_bar)

    def _add_background(self, widget, color, radius=None):
        with widget.canvas.before:
            Color(*color)
            if radius:
                widget.bg_rect = RoundedRectangle(size=widget.size, pos=widget.pos, radius=radius)
            else:
                widget.bg_rect = Rectangle(size=widget.size, pos=widget.pos)
        widget.bind(size=self._update_bg_rect, pos=self._update_bg_rect)

    def _update_bg_rect(self, instance, value):
        instance.bg_rect.pos = instance.pos
        instance.bg_rect.size = instance.size

    def submit_text(self, instance):
        user_message = self.text_input.text.strip()
        if user_message:
            self._add_message(user_message, is_user=True)
            self._add_message("Hello! I'm your DreamMate.", is_user=False)
            self.text_input.text = ""

    def _add_message(self, message, is_user):
        if is_user:
            alignment = 'right'
            color = (0.9, 0.9, 1, 1)
        else:
            alignment = 'left'
            color = (0.8, 0.8, 0.8, 1)

        message_label = Label(
            text=message,
            size_hint_y=None,
            halign=alignment,
            valign='middle',
            color=(0, 0, 0, 1),
            font_name='resources/poppins.ttf',
        )

        message_label.text_size = (self.scroll_view.width * 0.9, None)
        message_label.bind(texture_size=self._adjust_label_height)

        with message_label.canvas.before:
            Color(*color)
            message_label.bg_rect = Rectangle(size=message_label.size, pos=message_label.pos)

        message_label.bind(size=self._update_bg_rect, pos=self._update_bg_rect)

        self.messages_layout.add_widget(message_label)

    def _adjust_label_height(self, instance, value):
        instance.height = instance.texture_size[1] + 10


    def save_chat(self, instance):
        chat_content = [
            {"text": child.text, "is_user": 'right' in child.halign}
            for child in self.messages_layout.children[::-1]
        ]
        self.chat_logs.append(chat_content)

        entry_number = len(self.chat_logs)
        entry_box = BoxLayout(size_hint=(1, None), height=50)
        self._add_background(entry_box, (0.378, 0.350, 0.555, 1), radius=[10])

        number_label = Label(text=str(entry_number), size_hint=(1, 1), halign='center', valign='middle')
        number_label.text_size = number_label.size
        entry_box.add_widget(number_label)

        entry_box.bind(on_touch_down=partial(self._on_entry_touch, entry_number=entry_number))

        self.left_grid.add_widget(entry_box)

        self._save_chats_to_file()

    def _on_entry_touch(self, instance, touch, entry_number):
        if instance.collide_point(*touch.pos):
            self.load_chat(entry_number)

    def _save_chats_to_file(self):
        with open(self.DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(self.chat_logs, file, ensure_ascii=False, indent=4)

    def _load_chats_from_file(self):
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, "r", encoding="utf-8") as file:
                self.chat_logs = json.load(file)

    def _populate_journal_entries(self):
        for i, chat in enumerate(self.chat_logs, start=1):
            entry_box = BoxLayout(size_hint=(1, None), height=50)
            self._add_background(entry_box, (0.378, 0.350, 0.555, 1), radius=[10])
            
            number_label = Label(text=str(i), size_hint=(1, 1), halign='center', valign='middle')
            number_label.text_size = number_label.size
            entry_box.add_widget(number_label)
            entry_box.bind(on_touch_down=lambda instance, touch, idx=i: self.load_chat(idx) if instance.collide_point(*touch.pos) else None)
            
            self.left_grid.add_widget(entry_box)

    def load_chat(self, entry_number):
        self.messages_layout.clear_widgets()

        for message in self.chat_logs[entry_number - 1]:
            self._add_message(message["text"], is_user=message["is_user"])


    def start_new_chat(self, instance):
        self.messages_layout.clear_widgets()
        self.text_input.text = ""

ChatApp().run()
