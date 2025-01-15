import json
import os
from functools import partial
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.image import Image
from modules.interpretation import create_interpretation
from modules.recommendation import generate_recommendation
from modules.use_sentiment_analysis_model import predict_emotion
from modules.use_sentiment_analysis_jhartman import predict_emotions
from modules.generate_dream_title import generate_dream_title

Window.size = (900, 600) 

class ChatApp(App):
    DATA_FILE = "chat_logs.json"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.emotion_labels = {}
        self.last_predicted_emotions = {}
        self.dream_title = ""

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
        self._add_background(self.left_layout, (0.278, 0.250, 0.555, 1))

        self.left_scroll = ScrollView(size_hint=(1, 1))
        self.left_grid = GridLayout(cols=1, size_hint_y=None, spacing=10, padding=10)
        self.left_grid.bind(minimum_height=self.left_grid.setter('height'))

        self.left_scroll.add_widget(self.left_grid)
        self.left_layout.add_widget(self.left_scroll)
        self.root_layout.add_widget(self.left_layout)

        self._populate_journal_entries()

    def _populate_journal_entries(self):
        for i, chat_data in enumerate(self.chat_logs, start=1):
            entry_box = BoxLayout(size_hint=(1, None), height=100)
            self._add_background(entry_box, (0.378, 0.350, 0.655, 1), radius=[10])

            dream_title = chat_data.get("dream_title", f"Dream {i}")
            
            title_label = Label(
                text=dream_title,
                size_hint=(1, None),
                halign='center',
                valign='middle',
                font_name='resources/poppins-med.ttf'
            )
            title_label.text_size = title_label.size
            entry_box.add_widget(title_label)

            entry_box.bind(on_touch_down=partial(self._on_entry_touch, entry_number=i))

            entry_box.bind()
            
            self.left_grid.add_widget(entry_box)

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
            padding=[10, 10, 10, 10],
            orientation='horizontal',
        )

        self._add_background(self.top_bar, (0.278, 0.250, 0.555, 1))

        dreammate_label = Label(
            text="DreamMate",
            size_hint=(None, 1),
            width=350,
            halign='left',
            valign='middle',
            font_name='resources/timeburnerbold.ttf',
            font_size='30sp',
            color=(1, 1, 1, 1),
            padding = [10, 10, 10, 130]
        )
        dreammate_label.bind(texture_size=self._adjust_label_size)
        dreammate_label.text_size = (dreammate_label.width, None)
        self.top_bar.add_widget(dreammate_label)

        #self.top_bar.add_widget(Widget(size_hint=(1, 1)))

        central_layout = BoxLayout(
            orientation='horizontal',
            size_hint=(None, None),
            spacing=20,
            pos_hint={'center_x': 0.8, 'center_y': 0.5}
        )

        emotions = [
            ("resources/happy.png", "0%", "happiness"),
            ("resources/sad.png", "0%", "sadness"),
            ("resources/anger.png", "0%", "anger"),
            ("resources/fear.png", "0%", "fear"),
        ]
        for icon, percentage, emotion_key in emotions:
            self._create_emotion_widget(icon, percentage, central_layout, emotion_key)

        self.new_button = Button(
            text="Start fresh",
            size_hint=(None, None),
            size=(120, 60),
            background_color=(0.278, 0.250, 0.455, 1),
            color=(0.9, 0.9, 1, 1),
            font_name='resources/poppins.ttf',
        )

        self.new_button.bind(on_press=self.start_new_chat)

        central_layout.add_widget(self.new_button)

        self.top_bar.add_widget(central_layout)
        self.top_bar.add_widget(Widget(size_hint=(1.5, 1)))

        self.right_layout.add_widget(self.top_bar)


    def _create_emotion_widget(self, icon_source, percentage, parent_layout, emotion_key):
        layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(80, 120))
        icon = Image(source=icon_source, size_hint=(None, None), size=(70, 70), pos_hint={"center_y": 0.5})
        label = Label(text=percentage, size_hint=(1, None), height=20, halign='center')
        label.text_size = (label.width, None)

        layout.add_widget(icon)
        layout.add_widget(label)

        parent_layout.add_widget(layout)

        self.emotion_labels[emotion_key] = label

    def _create_chat_area(self):
        self.scroll_view = ScrollView(size_hint=(1, 1))
        self._add_background(self.scroll_view, (0.278, 0.250, 0.555, 1))

        self.messages_layout = GridLayout(cols=1, size_hint_y=None, spacing=10)
        self.messages_layout.bind(minimum_height=self.messages_layout.setter('height'))

        self.scroll_view.add_widget(self.messages_layout)
        self.right_layout.add_widget(self.scroll_view)

    def _create_bottom_bar(self):
        self.bottom_bar = BoxLayout(size_hint_y=None, height=130)

        self.text_input = TextInput(
            hint_text="Describe your dream and well-being...",
            multiline=True,
            foreground_color=(0, 0, 0, 1),
            background_color=(0.9, 0.9, 1, 1),
            font_size=16,
            padding=[10, 10],
            font_name='resources/poppins.ttf',
            background_normal='',
            background_active=''
        )
        self.text_input.size_hint_x = 0.8

        self.send_button = Button(
            text="Send",
            size_hint_x=0.1,
            background_color=(0.278, 0.250, 0.455, 1),
            color=(0.9, 0.9, 1, 1),
            font_name='resources/poppins.ttf'
        )
        self.send_button.bind(on_press=self.submit_text)

        self.save_button = Button(
            text="Save",
            size_hint_x=0.1,
            background_color=(0.278, 0.250, 0.455, 1),
            color=(0.9, 0.9, 1, 1),
            font_name='resources/poppins.ttf'
        )
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

    def _adjust_label_height(self, instance, value):
        instance.height = instance.texture_size[1] + 10

    def _adjust_label_size(self, instance, value):
        instance.text_size = (instance.width, None)

    def submit_text(self, instance):
        user_message = self.text_input.text.strip()
        if not user_message:
            return

        self._add_message(user_message, is_user=True)

        self.dream_title = generate_dream_title(user_message)

        try:
            interpretation = create_interpretation(user_message)
        except Exception:
            interpretation = "Sorry, I couldn't analyze your dream. Please try again."
        self._add_message(
            f"Discover the Meaning of Your Dream with DreamMate\n\n"
            f"{interpretation}",
            is_user=False
        )

        recommendation = generate_recommendation(user_message)
        self._add_message(
            f"DreamMate's Secrets to a Restful Night\n\n"
            f"{recommendation}",
            is_user=False
        )

        predicted_emotions = predict_emotion(user_message)
        self.last_predicted_emotions = predicted_emotions

        for emotion, percentage in predicted_emotions.items():
            if emotion in self.emotion_labels:
                self.emotion_labels[emotion].text = f"{int(percentage)}%"

        emotions_text = "\n".join([
            f"{emotion.capitalize()}: {int(percent)}%"
            for emotion, percent in predicted_emotions.items()
        ])
        self._add_message(
            f"Emotions Revealed by DreamMate\n\n"
            f"{emotions_text}",
            is_user=False
        )

        self.text_input.text = ""

    def _add_message(self, message, is_user):
        if is_user:
            alignment = 'right'
            bg_color = (0.9, 0.9, 1, 1)
            text_color = (0, 0, 0, 1)
        else:
            alignment = 'left'
            bg_color = (0.75, 0.70, 0.9, 1)
            text_color = (0, 0, 0, 1)

        message_label = Label(
            text=message,
            size_hint_y=None,
            halign=alignment,
            valign='middle',
            color= text_color,
            font_name='resources/poppins-med.ttf'
        )
        message_label.text_size = (self.scroll_view.width * 0.9, None)
        message_label.bind(texture_size=self._adjust_label_height)

        with message_label.canvas.before:
            Color(*bg_color)
            message_label.bg_rect = RoundedRectangle(size=message_label.size, pos=message_label.pos, radius=[15])
        
        message_label.bind(size=self._update_bg_rect, pos=self._update_bg_rect)

        self.messages_layout.add_widget(message_label)

    def save_chat(self, instance):
        chat_content = [
            {"text": child.text, "is_user": ('right' in child.halign)}
            for child in self.messages_layout.children[::-1]
        ]

        chat_data = {
            "messages": chat_content,
            "predicted_emotions": self.last_predicted_emotions,
            "dream_title": self.dream_title
        }
        self.chat_logs.append(chat_data)

        entry_box = BoxLayout(size_hint=(1, None), height=100)
        self._add_background(entry_box, (0.378, 0.350, 0.655, 1), radius=[10])

        title_label = Label(
            text=self.dream_title,
            size_hint=(1, None),
            halign='center',
            valign='middle',
            font_name='resources/poppins-med.ttf'
        )

        title_label.text_size = title_label.size
        entry_box.add_widget(title_label)

        current_entry_number = len(self.chat_logs)
        entry_box.bind(on_touch_down=partial(self._on_entry_touch, entry_number=current_entry_number))
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

    def load_chat(self, entry_number):
        self.messages_layout.clear_widgets()

        chat_data = self.chat_logs[entry_number - 1]
        messages = chat_data.get("messages", [])
        predicted_emotions = chat_data.get("predicted_emotions", {})
        self.dream_title = chat_data.get("dream_title", "")

        for message in messages:
            self._add_message(message["text"], is_user=message["is_user"])

        for emotion in self.emotion_labels:
            value = int(predicted_emotions.get(emotion, 0))
            self.emotion_labels[emotion].text = f"{value}%"
        self.last_predicted_emotions = predicted_emotions

    def start_new_chat(self, instance):
        self.messages_layout.clear_widgets()
        self.text_input.text = ""

        self.last_predicted_emotions = {}
        for emotion_key, label in self.emotion_labels.items():
            label.text = "0%"

        self.dream_title = ""

if __name__ == "__main__":
    ChatApp().run()
