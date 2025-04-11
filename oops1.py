class employee:
    ## special method / magic method / constructor
    def __init__(self):
        print("Always gets called")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"

    ## function
    def travel(self , destination):
        print(f"employee is now travelling to {destination}")

## creating ans object / instance of the class
sam = employee()

## print(sam.id)

## sam.travel("Bihar")

print(type(sam))


