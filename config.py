from dotenv import dotenv_values

DEBUG_MODE = True

config = dotenv_values(".env.dev" if DEBUG_MODE else ".env")

TOKEN = config["TOKEN"]