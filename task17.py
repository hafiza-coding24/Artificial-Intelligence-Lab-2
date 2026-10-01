class person:
    def __init__(self,name,age):
      self.age=age
      self.name=name
def myfunc(self):
    print("Hello my name is " + self.name)
p1=person("john", 36)
myfunc(p1)