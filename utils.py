from dotenv import dotenv_values

config = dotenv_values()


def get_config(name):
    return config.get(name, None)
