# Create custom int subclass, returning new instance of itself with updated value
class CustomInt(int):
    def __call__(self, v):  # Allows instance to be 'called' as a function
        return CustomInt(self + v)
    
def add(v):
    return CustomInt(v)

add(1)(2)(3)