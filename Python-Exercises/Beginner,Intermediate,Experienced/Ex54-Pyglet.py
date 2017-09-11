import pyglet as pg

window = pg.window.Window()
label = pg.text.Label('Hello,World',
                      font_name='Times New Roman',
                      font_size=40,
                      x=window.width//2,y=window.height//2,
                      anchor_x='center',anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()

pg.app.run()
