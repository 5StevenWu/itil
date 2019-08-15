import os
import sys
ret = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,ret)



if __name__ == '__main__':

    os.environ['USER_SETTINGS'] = 'conf.settings'
    from src.script import run
    run()
