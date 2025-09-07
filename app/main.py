class HelloWorld:
    def __init__(self):
        pass
    
    def hello(self):
        print("Hello world! This is my firts Python Project!")

def main():
    print("Script Started")
    my_object=HelloWorld()
    my_object.hello()
    print("Script Finished")

if __name__ == "__main__":
    main()