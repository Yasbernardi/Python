"""***Qual é a causa do problema?***
R: A propriedade da classe mãe é privada, para resolver o problema é só tornar a propriedade uma classe protegida.
"""
class usuario():
  _nomeUsuario = ""

  def setnome(self, nome):
    self._nome = nome

class admin(usuario):

  def escrevaNome(self):
    return "Admin"
  def digaOla(self):
    return "Olá Admin," + self._nome

admin1 = admin()
admin1.setnome("Baltazar")
print (admin1.digaOla())


