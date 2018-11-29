import pygame
import render
import mouse
import keyboard
import event
import loop
import scene

pygame.init()

renderer = render.Renderer((800, 500))
mouse = mouse.Mouse()
keyboard = keyboard.Keyboard()
handler = event.Handler(mouse, keyboard)
scene = scene.Scene(mouse, keyboard)

loop = loop.Loop(renderer, handler, scene)

while not loop.update():
	pass

pygame.quit()
