from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import platform

class IPOneLite(App):
    def build(self):
        status = "300MB/Day WhatsApp Bridge: ACTIVE"
        wallet = "Linked to Mr. Swartz (49vGTF...)"
        return Label(text=f"IP ONE LITE\n{status}\n{wallet}\nHigh Earning: ENABLED", halign="center")

if __name__ == "__main__":
    IPOneLite().run()