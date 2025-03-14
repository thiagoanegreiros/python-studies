import time

def get_instantiation_time(self):
    return self.instantiation_time

class MPType(type):
    classes_guarded: list[str] = [1]

    def __new__(mcs, name, bases, dictionary):
        if 'get_instantiation_time' not in dictionary:
            dictionary['get_instantiation_time'] = get_instantiation_time
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.instantiation_time = time.time()
        MPType.classes_guarded.append(name)
        time.sleep(1)
        return obj
    
class C1(metaclass=MPType):
    pass
class C2(metaclass=MPType):
    pass

obj1 = C1()
print(obj1.instantiation_time)

obj2 = C2()
print(obj2.instantiation_time)

print(MPType.classes_guarded)