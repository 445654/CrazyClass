import pygame
import render
import config

renderer = render.Renderer(config.SCREEN_SIZE, config.ROOM_SIZE)

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
