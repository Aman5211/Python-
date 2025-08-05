class employees:
    a=1

    @classmethod
    def show(cls):
        print(f"The class attribute of a id {cls.a}")

e=employees()
e.a=45 #instance attribute is not working in the cls argument 

e.show()

#Property Decorator
# Ye samaj mei nhi aa rha tha bilkul bhi 
