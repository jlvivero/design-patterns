import inspect
class my_class(object):
    def __init__(self):
        self.id = 0
        self.name = ""
        self.cal = 100.0


variable = my_class()
print"CREATE TABLE", type(variable).__name__
print("(")
tatt = vars(variable)
i = 0
for key in tatt:
    if type(tatt[key]).__name__ == "str":
        print key,"varchar", "(256)", "DEFAULT","'",tatt[key], "'"
    elif type(tatt[key]).__name__ == "float":
        print key, "decimal", "(8)", "DEFAULT", tatt[key]
    else:
        print key, type(tatt[key]).__name__, "DEFAULT", tatt[key]
    if i < len(tatt) - 1:
        print ","
    i = i + 1

print (");")
