from pico2d import*
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
while(1):
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.001)

    while (y < 590):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 2
        delay(0.001)

    while (x > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        delay(0.001)
        
    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 2
        delay(0.001)

    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.001)
        
    x = -180
    while (x <= 180):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(400+390*math.sin(x/360 * -2 * math.pi),300 + 210*math.cos(x/360*-2*math.pi))
        x = x + 2
        delay(0.001)

close_canvas()
