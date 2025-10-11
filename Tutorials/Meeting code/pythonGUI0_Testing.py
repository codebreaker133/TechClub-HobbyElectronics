from guizero import App, Text

app = App(title= "girst gui") # title for window

message = Text(app, text="this is a GUI")
first_message = Text(app, text="this is large text")
second_message = Text(app, text="this is white text")
first_message.text_size = 40
second_message.text_color = "white"
second_message.bg = "black"
second_message.text_size = 20

app.display()

