from guizero import App, PushButton, Window, Text, Combo, PushButton, info, Window
app = App()
Message_1 = Text(app, text= "Welcome to the online travel portal! Please submit, when reaady!", size = 10)

def do_nothing():
    print("Operating Correctly")
    window = Window(app, title = "HitTheSkies.com")

Ouch = PushButton(app, command=do_nothing, text = "Submit")



app.display()