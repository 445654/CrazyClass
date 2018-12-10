import pygame
import render
renderer = render.Renderer((800, 500))

import mouse
import keyboard
import event
import loop
import scene

pygame.init()

mouse = mouse.Mouse()
keyboard = keyboard.Keyboard()
handler = event.Handler(mouse, keyboard)
scene = scene.Scene(mouse, keyboard)

loop = loop.Loop(renderer, handler, scene)

while not loop.update():
	pass

pygame.quit()
