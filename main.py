from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from ursina import *
import sys      

# Player
class Player(PlatformerController2d):
    def __init__(self, pos=(0,0)):
        super().__init__(
            # Visual
            texture = "white_cube",
            color = color.red,
            
            # Position and Scale
            position = pos,
            scale_x = 1,
            scale_y = 2,
            
            # Collider
            collider = "box"
        )   
    
# Block
class Block(Button):
        def __init__(self, position=(0,0), texture="assets/textures/grass_block.png"):
            super().__init__(
                # Button Parent
                parent = scene,
            
                # Model and Texture
                model = "quad",
                texture = texture,
            
                # Position 
                position = position,
            
                # Color
                color = color.white,
                highlight_color = color.gray
        )
    
        def input(self, key):
            if self.hovered:
                # Break Block
                if key == "right mouse down":
                    destroy(self)
                
                # Place Blocks
                # Grass
                if block == 1:
                    # Up
                    if key == "8":
                        Block(position = self.position + (0,1), texture = grass_block) 
                    if key == "up arrow":
                        Block(position = self.position + (0,1), texture = grass_block)
                        
                    # Down
                    if key == "2":
                        Block(position = self.position + (0,-1), texture = grass_block)  
                    if key == "down arrow":
                        Block(position = self.position + (0,-1), texture = grass_block) 
                    
                    # Right
                    if key == "6":
                        Block(position = self.position + (1,0), texture = grass_block)  
                    if key == "right arrow":
                        Block(position = self.position + (1,0), texture = grass_block)
                 
                    # Left     
                    if key == "4":
                        Block(position = self.position + (-1,0), texture = grass_block)  
                    if key == "left arrow":
                        Block(position = self.position + (-1,0), texture = grass_block)
                
                # Dirt
                if block == 2:
                    # Up
                    if key == "8":
                        Block(position = self.position + (0,1), texture = dirt_block) 
                    if key == "up arrow":
                        Block(position = self.position + (0,1), texture = dirt_block)  
                    
                    # Down
                    if key == "2":
                        Block(position = self.position + (0,-1), texture = dirt_block)  
                    if key == "down arrow":
                        Block(position = self.position + (0,-1), texture = dirt_block)
                        
                    # Right
                    if key == "6":
                        Block(position = self.position + (1,0), texture = dirt_block)  
                    if key == "right arrow":
                        Block(position = self.position + (1,0), texture = dirt_block)
                 
                    # Left     
                    if key == "4":
                        Block(position = self.position + (-1,0), texture = dirt_block)  
                    if key == "left arrow":
                        Block(position = self.position + (-1,0), texture = dirt_block)
                
                # Dark Oak Log
                if block == 3:
                    # Up
                    if key == "8":
                        Block(position = self.position + (0,1), texture = dark_oak_log) 
                    if key == "up arrow":
                        Block(position = self.position + (0,1), texture = dark_oak_log)  

                    # Down
                    if key == "2":
                        Block(position = self.position + (0,-1), texture = dark_oak_log)  
                    if key == "down arrow":
                        Block(position = self.position + (0,-1), texture = dark_oak_log)   
                    
                    # Right
                    if key == "6":
                        Block(position = self.position + (1,0), texture = dark_oak_log)  
                    if key == "right arrow":
                        Block(position = self.position + (1,0), texture = dark_oak_log)
                 
                    # Left     
                    if key == "4":
                        Block(position = self.position + (-1,0), texture = dark_oak_log)  
                    if key == "left arrow":
                        Block(position = self.position + (-1,0), texture = dark_oak_log)
            
# UI
app = Ursina()
window.fullscreen = True
window.cog_button.visible = False 

# Textures
grass_block = load_texture("assets/textures/grass_block.png")
dirt_block = load_texture("assets/textures/dirt.png")
dark_oak_log = load_texture("assets/textures/dark_oak_log.png")

# Inventory
block = 1

def update():
    global block
    if held_keys["1"]:
        block = 1
        #grass = Text(parent = camera.ui, text = "(1) Grass Block", scale = 2, origin = (2.1, -9), text_color = "white")
    if held_keys["2"]:
        block = 2
        #dirt = Text(parent = camera.ui, text = "(2) Dirt Block", scale = 2, origin = (2.5, -9), text_color = "white")
    if held_keys["3"]:
        block = 3
        #dark_log = Text(parent = camera.ui, text = "(3) Dark Oak Log", scale = 2, origin = (1.8, -9), text_color = "white")

# World 
Block(position = (0,0))

# Camera
camera.parent = scene
camera.fov = 40

# Input
def input(key):
        # Quit Game
        if key == "escape":
            sys.exit(0) 
        
        # Spawn Player
        if key == "middle mouse down":
            player = Player(pos = (0,5))   
            camera.add_script(SmoothFollow(target=player, offset=[0,1,-30])) 
        
        # Camera Zoom        
        if key == "-":
            camera.fov += 10
        if key == "+":
            camera.fov -= 10   
           
app.run()
