import pygame
import render
import mouse
import keyboard
import event
import loop
import scene

pygame.init()

renderer = render.Renderer((500, 500))
mouse = mouse.Mouse()
keyboard = keyboard.Keyboard()
handler = event.Handler(mouse, keyboard)
scene = scene.Scene()

loop = loop.Loop(renderer, handler)

while loop.update():
	pass

pygame.quit()
