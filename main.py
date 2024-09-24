# class student:
#     grade=10
#     name="akshath"
#     def intro(self):
#         print("hello i am",self.name,"i am in",self.grade)

# obj=student()
# obj.intro()

class parrot:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        return self.name,"sings a nice song"

parrot1=parrot("kili",10)
print(parrot1.sing("happy"))