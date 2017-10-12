from cx_Freeze import setup, Executable

setup(
    name = "IAR - Homework 1",
    version = "1.0",
    description = "Reinforcement learning algorithms simulations",
    executables = [Executable("main.py")],
)
