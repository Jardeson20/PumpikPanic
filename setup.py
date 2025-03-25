from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

setup(
    name="Pumpik Panic",
    version="1.0",
    description="Pumpik Panic app, o jogo da abóbora do pânico",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables
)