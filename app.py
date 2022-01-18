import eel


@eel.expose
def build(elements):
    res = f"hello hell :){elements}"
    print(res)
    return res


eel.init('front', allowed_extensions=['.js', '.html'])


@eel.expose  # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)


say_hello_py('Python World!')
eel.say_hello_js('Python World!')  # Call a Javascript function

eel.start('canvas.html', mode="default")
