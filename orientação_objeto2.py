class Usuario:
  primeironome = "Jonnie"
  ultimonome = "Bravo"

  def hello(self):
    return "Olá, " + self.primeironome + " " + self.ultimonome

user1 = Usuario()
print (user1.hello())
