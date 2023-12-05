class English:
    def greet(self, name):
        print("good morning ", name)

class French:
    def greet(self, name):
        print("bonjour ", name)

def greeting(language, name):
    language.greet(name)

e = English()
f = French()

greeting(e, 'Ajith')
greeting(f, 'Anay')