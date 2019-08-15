import abc


class Person(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def talk(self):
        print('xx')


class Chinese(Person):
    pass
    # def talk(self):
    #     print('中国话')


class Person():

    def talk(self):
        raise NotImplementedError('talk()  must be Implemented')


class Chinese(Person):
    pass

    # def talk(self):
    #     print('中国话')

#
p = Chinese()
p.talk()
