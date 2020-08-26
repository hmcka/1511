# Explosion
# Demonstrates creating an animation

import sys, os, math
from livewires import games
from spriteUtils import *

games.init(screen_width = 640, screen_height = 480, fps = 50)

park_image = games.load_image("park-scene.png")
games.screen.background = park_image

walker_list = load_sliced_sprites(150, 200, 'walking_girl.png')

#filename = sys.argv[1]
#x = int(sys.argv[2])
#y = int(sys.argv[3])

#games.init(fps = 50)

#animation_list = load_2d_sheets(x, y, filename)
          
walker = games.Animation(images = walker_list,\
                            x = 275,\
                            y = 350,\
                            n_repeats = -1,\
                            repeat_interval = 15)
games.screen.add(walker)

games.screen.mainloop()
