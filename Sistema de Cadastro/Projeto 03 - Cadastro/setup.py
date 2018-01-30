from cx_Freeze import setup, Executable

setup(
    name = "Palindroma Program",
    version = "0.1",
    description = "Diz se a palavra é palindroma",
    executables = [Executable('challenge-053.py')]
)

