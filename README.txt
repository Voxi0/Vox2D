This is a 2D clone of Minecraft I made with Python 3.10.7 and the Ursina Game Engine.
I have used OOP concept to make things more organized and easier to manage. I built
the foundation(Building System, Camera, Blocks) etc.

Controls:
 	Player -
		MMB = Spawn Player (Always Spawn One)
		WASD = Move Player (Red Cube)
		Space = Jump

	Building -
		Up Arrow or 8 on Numpad = Place Block Above Block Cursor is Pointing At
		Down Arrow or 2 on Numpad = Place Block Below Block Cursor is Pointing At

		Right Arrow or 6 on Numpad = Place Block to the Right Side of the Block Cursor is Pointing At
		Left Arrow or 4 on Numpad = Place Block to the Left Side of the Block Cursor is Pointing At

		Press RMB to Delete Block That The Mouse Cursor is Pointing At

	Camera -
		Press + to Zoom In
		Press - to Zoom Out
	
	Textures -
		Currently, there are 3 textures in Vox2D. They are:
			1) Grass Block 
			2) Dirt Block 
			3) Dark Oak Log
		
		Pressing any of these numbers can change textures.

There is only one block in the world by default. You can just create new blocks to make your own map
to your liking by following the controls.
