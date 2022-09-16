from cx_Freeze import setup, Executable

target = Executable(
	script = "main.py",
	icon = "icon.ico"
)

setup(
    name="Minecraft 2D",
    version=1.0,
    description="2D Minecraft Clone in Ursina.",
    author = "BitterSweet",
    options={"build_exe": {"packages": ["ursina"]}},
    executables = [target]
)
