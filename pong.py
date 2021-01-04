# -*- coding: utf-8 -*-

import turtle
import random
import pygame
import time
import os

def tocar(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

altura = 600
largura = 1000
janela = turtle.Screen()
janela.title("Ping Pong")
janela.bgcolor("black")
janela.setup(width=largura, height=altura)
janela.tracer(0)

# Raquete A
raquete_a = turtle.Turtle()
raquete_a.speed(0)
raquete_a.shape("square")
raquete_a.color("white")
raquete_a.shapesize(stretch_wid=5, stretch_len=1)
raquete_a.penup()
raquete_a.goto(-450,0)


# Raquete B
raquete_b = turtle.Turtle()
raquete_b.speed(0)
raquete_b.shape("square")
raquete_b.color("white")
raquete_b.shapesize(stretch_wid=5, stretch_len=1)
raquete_b.penup()
raquete_b.goto(450,0)


# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0,0)
bola.dx = 0.3
bola.dy = 0.3

# Centro

centro = turtle.Turtle()
centro.speed(0)
centro.color("white")
centro.penup()
centro.goto(0,0)

# Placar
jogador1 = janela.textinput("Digite suas informações","Nome do 1º jogador:")
jogador2 = janela.textinput("Digite suas informações","Nome do 2º jogador:")
placar1 = 0
placar2 = 0

placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0,260)
placar.write("{}: {}    {}: {}".format(jogador1,placar1,jogador2,placar2), align="center", font=("Courier",24,"normal"))
# Funções

def raquete_a_CIMA():
    y = raquete_a.ycor()
    if y < 250:
        y += 20
        raquete_a.sety(y)

def raquete_a_BAIXO():
    y = raquete_a.ycor()
    if y > -240:
        y -= 20
        raquete_a.sety(y)
def raquete_b_CIMA():
    y = raquete_b.ycor()
    if y < 250:
        y += 20
        raquete_b.sety(y)

def raquete_b_BAIXO():
    y = raquete_b.ycor()
    if y > -240:
        y -= 20
        raquete_b.sety(y)

janela.listen()
janela.onkeypress(raquete_a_CIMA, "w")
janela.onkeypress(raquete_a_BAIXO, "s")
janela.onkeypress(raquete_b_CIMA, "Up")
janela.onkeypress(raquete_b_BAIXO, "Down")

# Main game loop

while True:
    janela.update()

    # Move a bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
        os.system("aplay som.wav&")
    if bola.xcor() > 490:
        bola.setx(490)
        bola.dx *= -1
        os.system("aplay som.wav&")
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
        os.system("aplay som.wav&")
    if bola.xcor() < -490:
        bola.setx(-490)
        bola.dx *= -1
        os.system("aplay som.wav&")
    if bola.xcor() > 485:
        tocar("som2.mp3")
        time.sleep(2)
        bola.goto(0, 0)
        bola.dx = random.choice([0.3,-0.3])
        bola.dy = random.choice([0.3,-0.3])
        placar1 += 1
        placar.clear()
        placar.write("{}: {}    {}: {}".format(jogador1, placar1, jogador2, placar2), align="center",font=("Courier", 24, "normal"))
    if bola.xcor() < -485:
        tocar("som2.mp3")
        time.sleep(2)
        bola.goto(0, 0)
        placar2 +=1
        placar.clear()
        placar.write("{}: {}    {}: {}".format(jogador1, placar1, jogador2, placar2), align="center",font=("Courier", 24, "normal"))
        bola.dx = random.choice([0.3,-0.3])
        bola.dy = random.choice([0.3,-0.3])


    if ((bola.ycor() > (raquete_a.ycor() - 60)) and (bola.ycor() < raquete_a.ycor() + 60)) and (bola.xcor() < -450) :
        os.system("aplay som.wav&")
        bola.dy *= -1
        bola.dx *= -1
        bola.dx = bola.dx + 0.1
        bola.dy = bola.dy + 0.1
    if ((bola.ycor() > (raquete_b.ycor() - 60)) and (bola.ycor() < raquete_b.ycor() + 60)) and (bola.xcor() > 450):
        os.system("aplay som.wav&")
        bola.dy *= -1
        bola.dx *= -1
        bola.dx = bola.dx - 0.1
        bola.dy = bola.dy - 0.1
