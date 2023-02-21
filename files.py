class Test:
    def main():
        a=str(input("Write Something -> "))
        f = open("demofile.txt", "x")
        f=open("demofile.txt","w")
        f.write(a)
        f.close()
        f = open("demofile.txt", "r")
        print(f.read())
Test.main()