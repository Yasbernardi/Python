# -*- coding: utf-8 -*-
"""Orientação Objeto2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TGPhqxGLHeXOJY41utBB7LHytTxMQskq
"""

class Usuario:
  primeironome = "Jonnie"
  ultimonome = "Bravo"

  def hello(self):
    return "Olá"

usuario1 = Usuario()
print (usuario1.hello(), usuario1.primeironome, usuario1.ultimonome)