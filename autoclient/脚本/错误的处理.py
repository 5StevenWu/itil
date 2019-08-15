import traceback


def disk():
    int('saaa')


def run():
    try:
        disk()
    except Exception:
        ret = traceback.format_exc()
        print(ret)
        print(type(ret))

run()