# # for i in range(1,11):
# #     print(i)
# i = 1
# while i <= 11:
#     print(i)
#     i = +1
import pip


def install(package):
    pip.main(['install', package])

# Example
if __name__ == '__main__':
    install('django')
