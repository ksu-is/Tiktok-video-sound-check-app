from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class TikTokScanner(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6,0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        #add widgets to window
        self.image = Image(source= "scannerlogo.png")
        self.window.add_widget (self.image)

        self.instruction = Label (text= "Enter the Tiktok profile link below:", color = '#69C9D0', font_size = 20, size_hint = (1,0.8))
        self.window.add_widget (self.instruction)
        
        #user profile link input
        self.user = TextInput( multiline= False, padding_y =(20,20), size_hint = (1,0.5))
        self.window.add_widget(self.user)

        #button widget
        self.button = Button (text= "SCAN", bold= True, background_color= 'EE1D52', background_normal="", padding_y =(20,20), size_hint = (1,0.5))
        self.window.add_widget (self.button)

        return self.window

        return self.window

if __name__ == "__main__":
    TikTokScanner().run()