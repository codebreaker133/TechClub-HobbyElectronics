import guizero

from guizero import  App, Text, TextBox, PushButton, info

app = App(title="gui test")

def btn_pres(txt_box):
    info("my box", "hello "+txt_box.value+" hope you are having a nice day!")


lbl_name = Text(app, text="wat is your name?")
txt_box = TextBox(app)

btn_action = PushButton(app, command=btn_pres(txt_box), text="click me!")

app.display()