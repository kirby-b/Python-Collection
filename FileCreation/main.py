class PyFileMaker:
  def main():
    print("This program will create a .py file with basic setup, if you want it to be in a different location you should add it before the name. Dont give it a file extension")
    name = input("File Name: ")
    name = name + ".py"
    #Gets the file name and concats .py to the end
    PyFileMaker.makeFile(name)
  
  
  def makeFile(name):
    f = open(name, "w")
    #Opens the file at the given location
    f.write("""class BasicClass():
    def __init__(self, value):
        self.value = value
    def main(self):
        pass #Main code stuff goes here. Usually for calls and basic stuff
    def new_func(self):
        pass #Modular special code goes here. Usually for things that need to be done more than once and more complicated things
if __name__ == "__main__":
     BasicClass.main()
""")
    #Creates the file with basic stuff
  
  
if __name__ == "__main__":
    PyFileMaker.main()