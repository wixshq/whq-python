# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i * i
#         fs.append(f)
#     return fs
# f1, f2, f3 = count()
#
# print f1(), f2(), f3()
# print count.__name__


class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_name(self,name):
        self.__name = name
    def set_score(self,score):
        if 0<=score<=100:
            self.__score = score
        else:
            raise ValueError('bad score')

    # def get_grade(self):
    #     if self.score>=90:
    #         print 'A'
    #     elif self.score>=60:
    #         print 'B'
    #     else:
    #         print 'C'

    def print_score(self):
        print ('%s:%s'%(self.__name,self.__score))

bart = Student('wixshq',60)
# # print bart.get_name(),bart.get_score()
# bart.set_score(-10)
# print bart.get_score()

print bart._Student__name



