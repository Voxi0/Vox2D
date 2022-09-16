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
                
                # Place Block Vertically
                # Up
                if key == "8":
                    Block(position = self.position + (0,1)) 
                if key == "up arrow":
                    Block(position = self.position + (0,1))        
            
                # Down    
                if key == "2":
                    Block(position = self.position + (0,-1))  
                if key == "down arrow":
                    Block(position = self.position + (0,-1))          
            
                # Place Block Horizontally
                # Right
                if key == "6":
                    Block(position = self.position + (1,0))  
                if key == "right arrow":
                    Block(position = self.position + (1,0))
                 
                # Left     
                if key == "4":
                    Block(position = self.position + (-1,0))  
                if key == "left arrow":
                    Block(position = self.position + (-1,0))
    
# UI
app = Ursina()
window.fullscreen = True
window.cog_button.visible = False 

# Textures
grass_block = load_texture("assets/textures/grass_block.png")

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
