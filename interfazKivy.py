from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle


class TransparentBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [10, 20, 10, 20]  # izquierda, arriba, derecha, abajo
        self.spacing = 5  # Menor separación
        self.size_hint = (None, None)
        self.size = (320, 250)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Fondo semitransparente
        with self.canvas.before:
            Color(1, 1, 1, 0.2)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

        # Widgets dentro del cuadro
        self.add_widget(Label(text="Login", font_size=24, size_hint_y=None, height=40))
        self.add_widget(TextInput(hint_text="Username", size_hint_y=None, height=30))
        self.add_widget(TextInput(hint_text="Password", password=True, size_hint_y=None, height=30))
        self.add_widget(Button(text="Login", size_hint_y=None, height=35))

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos



class LoginApp(App):
    def build(self):
        root = FloatLayout()

        # Imagen de fondo
        background = Image(source="fondoCubico.png", allow_stretch=True, keep_ratio=False)
        root.add_widget(background)

        # Cuadro de login
        login_box = TransparentBox()
        root.add_widget(login_box)

        return root


if __name__ == "__main__":
    LoginApp().run()
