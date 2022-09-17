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
                    if key == "up arrow":
                        Block(position = self.position + (0,1), texture = grass_block)
                        
                    # Down
                    if key == "down arrow":
                        Block(position = self.position + (0,-1), texture = grass_block) 
                    
                    # Right 
                    if key == "right arrow":
                        Block(position = self.position + (1,0), texture = grass_block)
                 
                    # Left     
                    if key == "left arrow":
                        Block(position = self.position + (-1,0), texture = grass_block)
                
                # Dirt
                if block == 2:
                    # Up
                    if key == "up arrow":
                        Block(position = self.position + (0,1), texture = dirt_block)  
                    
                    # Down
                    if key == "down arrow":
                        Block(position = self.position + (0,-1), texture = dirt_block)
                        
                    # Right 
                    if key == "right arrow":
                        Block(position = self.position + (1,0), texture = dirt_block)
                 
                    # Left     
                    if key == "left arrow":
                        Block(position = self.position + (-1,0), texture = dirt_block)
                
                # Dark Oak Log
                if block == 3:
                    # Up
                    if key == "up arrow":
                        Block(position = self.position + (0,1), texture = dark_oak_log)  

                    # Down 
                    if key == "down arrow":
                        Block(position = self.position + (0,-1), texture = dark_oak_log)   
                    
                    # Right
                    if key == "right arrow":
                        Block(position = self.position + (1,0), texture = dark_oak_log)
                 
                    # Left     
                    if key == "left arrow":
                        Block(position = self.position + (-1,0), texture = dark_oak_log)
                    
                # Cobblestone
                if block == 4:
                    # Up
                    if key == "up arrow":
                        Block(position = self.position + (0,1), texture = cobblestone)  

                    # Down 
                    if key == "down arrow":
                        Block(position = self.position + (0,-1), texture = cobblestone)   
                    
                    # Right
                    if key == "right arrow":
                        Block(position = self.position + (1,0), texture = cobblestone)
                 
                    # Left     
                    if key == "left arrow":
                        Block(position = self.position + (-1,0), texture = cobblestone)

app = Ursina()

# UI
window.title = "Vox2D"
window.icon = "icon.ico"
window.borderless = False
window.show_ursina_splash = True
window.fullscreen = True
window.render_mode = "default"
window.cog_button.visible = False 

# Camera
camera.parent = scene
camera.fov = 40

# Player
player = Player(pos = (0,5))   
camera.add_script(SmoothFollow(target=player, offset=[0,1,-30])) 

# Textures
grass_block = load_texture("assets/textures/grass_block.png")
dirt_block = load_texture("assets/textures/dirt.png")
dark_oak_log = load_texture("assets/textures/dark_oak_log.png")
cobblestone = load_texture("assets/textures/cobblestone.png")

# Inventory
block = 1

def update():
    global block
    # Grass
    if held_keys["1"]:
        block = 1
        #grass = Text(parent = camera.ui, text = "(1) Grass Block", scale = 2, origin = (2.1, -9), text_color = "white")
        
    # Dirt
    if held_keys["2"]:
        block = 2
        #dirt = Text(parent = camera.ui, text = "(2) Dirt Block", scale = 2, origin = (2.5, -9), text_color = "white")
        
    # Dark Oak Log
    if held_keys["3"]:
        block = 3
        #dark_log = Text(parent = camera.ui, text = "(3) Dark Oak Log", scale = 2, origin = (1.8, -9), text_color = "white")
    
    # Cobblestone
    if held_keys["4"]:
        block = 4

# World 
Block(position = (0,0))

# Input
def input(key):
        # Quit Game
        if key == "escape":
            sys.exit(0) 
        
        # Camera Zoom        
        if key == "-":
            camera.fov += 10
        if key == "+":
            camera.fov -= 10 
             
        # Change Render Mode
        if key == "h":
            window.render_mode = "default"
        if key == "j":
            window.render_mode = "wireframe"
        if key == "k":
            window.render_mode = "colliders"
           
app.run()
