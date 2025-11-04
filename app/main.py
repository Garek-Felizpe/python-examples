class HelloWorld:
    def __init__(self):
        pass

    def hello(self):
        print("Hello world! This is my firts Python Project!")


class Operator:
    a: int
    b: int

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def callOperator(self):
        equal = self.a == self.b  # False
        print("Este resultado deve ser igual a", equal)
        # print(f"Este resultado deve ser igual a:{equal}")
        different = self.a != self.b  # True
        print("Este resultado deve ser igual a", different)
        bigger_than = self.a > self.b  # True
        print("Este resultado deve ser igual a", bigger_than)
        smaller_than = self.a < self.b  # False
        print("Este resultado deve ser igual a", smaller_than)
        bigger_or_equal = self.a >= self.b  # True
        print("Este resultado deve ser igual a", bigger_or_equal)
        smaller_or_equal = self.a <= self.b  # False
        print("Este resultado deve ser igual a", smaller_or_equal)
        result_and = (self.a > 5) and (self.b < 5)  # True
        print("Este resultado deve ser igual a", result_and)
        result_or = (self.a > 15) or (self.b < 5)  # True
        print("Este resultado deve ser igual a", result_or)
        result_not = not (self.a > 5)  # False
        print("Este resultado deve ser igual a", result_not)


class Loop:
    pkm_inicial = ["Pikachu", "Squirtle", "Bubassauro", "Charmander"]

    def pokemon(self):

        for pokemon in self.pkm_inicial:
            print(pokemon)


def main():
    print("Script Started")

    hello_world = HelloWorld()
    hello_world.hello()
    operator = Operator()
    operator.callOperator()
    loop = Loop()
    print("Script Finished")


if __name__ == "__main__":
    main()
