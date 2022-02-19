# Runde Jia
# Sydeney
# 2021/11/24 13:52
class MyContentMgr(object):
    def __enter__(self):
        print('Enter method has been used')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit method has been used')

    def show(self):
        print('Show method has been used')


with MyContentMgr() as file:
    file.show()
