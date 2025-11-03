class HelloWorld:
    def __init__(self):
        pass
    
    def hello(self):
        print("Hello world! This is my firts Python Project!")

class Operator:
    def __init__(self):
        pass

    def callOperator(self):
        a = 10
        b = 3
        equal = a == b   # False
        print("Este resultado deve ser igual a",equal)
        # print(f"Este resultado deve ser igual a:{equal}")
        different = a != b   # True
        print("Este resultado deve ser igual a",different)
        bigger_than = a > b   # True
        print("Este resultado deve ser igual a",bigger_than)
        smaller_than = a < b   # False
        print("Este resultado deve ser igual a",smaller_than)
        bigger_or_equal = a >= b   # True
        print("Este resultado deve ser igual a",bigger_or_equal)
        smaller_or_equal = a <= b   # False
        print("Este resultado deve ser igual a",smaller_or_equal)
        result_and = (a > 5) and (b < 5)   # True
        print("Este resultado deve ser igual a",result_and)
        result_or = (a > 15) or (b < 5)   # True
        print("Este resultado deve ser igual a",result_or)
        result_not = not (a > 5)   # False
        print("Este resultado deve ser igual a",result_not)



def main():
    print("Script Started")
    my_object=HelloWorld()
    my_object.hello()
    my_object=Operator()
    my_object.callOperator()
    print("Script Finished")

if __name__ == "__main__":
    main()