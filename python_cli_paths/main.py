import fire


def hello(name="World"):
    return "Hello %s!" % name


# using entry points
def main():
    fire.Fire(hello)
