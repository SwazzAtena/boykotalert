from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class BoykotApp(App):
    def build(self):
        self.boykot_listesi = self.load_boykot_listesi("boykot_listesi.txt")

        # Layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Text Input
        self.text_input = TextInput(hint_text='Ürün adını girin...', font_size=20)
        layout.add_widget(self.text_input)

        # Button
        self.button = Button(text='Kontrol Et', font_size=20, background_color=(0.2, 0.6, 0.86, 1))
        self.button.bind(on_press=self.checkBoykot)
        layout.add_widget(self.button)

        # Label
        self.label = Label(text='', font_size=24)
        layout.add_widget(self.label)

        return layout

    def load_boykot_listesi(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return [line.strip().lower() for line in file]
        except FileNotFoundError:
            return []

    def checkBoykot(self, instance):
        product = self.text_input.text.strip().lower()
        if product in self.boykot_listesi:
            self.label.text = 'BOYKOT'
            self.label.color = (1, 0, 0, 1)
        else:
            self.label.text = 'DEĞİL'
            self.label.color = (0, 1, 0, 1)
        if(product == ""):
            self.label.text = 'LÜTFEN BOŞ BIRAKMAYINIZ'

if __name__ == '__main__':
    BoykotApp().run()
