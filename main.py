from kivy.app import App
from kivy.uix.button import Button


class TokiPonaKeyboardApp(App):
    def build(self):
        return Button(text="hello tokipona!!!")

if __name__ == "__main__":
    TokiPonaKeyboardApp().run()
