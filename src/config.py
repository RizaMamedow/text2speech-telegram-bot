from dotenv import dotenv_values

DEBUG_MODE = False

config = dotenv_values(".env.dev" if DEBUG_MODE else "env")

TOKEN = config["TOKEN"]