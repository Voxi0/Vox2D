from cx_Freeze import setup, Executable

target = Executable(
	script = "main.py",
	icon = "icon.ico"
)

setup(
    name="Vox2D",
    version=1.1,
    description="2D-Voxel Game Made With Python and Ursina.",
    author = "Voxi0",
    options={"build_exe": {"packages": ["ursina"]}},
    executables = [target]
)
