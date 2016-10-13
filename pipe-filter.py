class Filter():
    def __init__(self):
        self.list = None
        self.next = None
        self.input = None
        pass
    def execute(self, input):
        self.input = self.process(input)
        if self.next != None:
            self.next.execute(self.input)
    def register(self, filter):
        if self.next != None:
            self.next.register(filter)
        else:
            self.next = filter
    def process(self, input):
        raise NotImplementedError

class Pipeline():
    def __init__(self):
        self.root = None
        pass
    def execute(self, input):
        self.root.execute(input)
    def register(self, filter):
        if self.root ==  None:
            self.root = filter
        else:
            self.root.register(filter)

class UppercaseFilter(Filter):
    def __init__(self):
        self.list = None
        self.next = None
        pass
    def process(self, input):
        print(input.upper())
        return input.upper()

class LowercaseFilter(Filter):
    def __init__(self):
        self.list = None
        self.next = None
        pass
    def process(self, input):
        print(input.lower())
        return input.lower()

class ReversetextFilter(Filter):
    def __init__(self):
        self.list = None
        self.next = None
        pass
    def process(self, input):
        print(input[::-1])
        return(input[::-1])
#Main

words = "my data"
pipeline = Pipeline()
pipeline.register(ReversetextFilter())
pipeline.register(UppercaseFilter())
pipeline.register(LowercaseFilter())
pipeline.execute(words)
