"""class Test:
    def sit():
        a=float(input("Enter a number -> "))
        b=float(input("Enter second number -> "))
        xyz=a+b
        zyx=a-b
        yzx=a*b
        zxy=a/b
        print(round(xyz,2))
        print(round(zyx,2))
        print(round(yzx,2))
        print(round(zxy,2))
class Test_2(Test):
    pass
class Test_3(Test_2):
    pass
class Test_4(Test_3):
    pass
class Test_5(Test_4):
    pass
obj_inherit=Test_5
obj_inherit.sit()"""




#python program to display calendar

import calendar
class Calendar:
    def main():
        yy=int(input("Enter the Year -> "))
        mm=int(input("Enter the Month -> "))
        print(calendar.month(yy, mm))
Calendar.main()








