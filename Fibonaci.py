
# This class receive A,B = start and stop attributes and return Fibonaci sequences
class Fibonaci:
    def __init__(self,A,B,stop):
        self.A = A
        self.B = B
        self.stop = stop
        self.count = 0

    def __iter__(self):
         return self

    def __next__(self):
         print(self.A)
         print(self.B)
         while True:
          self.count = self.A + self.B
          if self.stop < self.count:
            raise StopIteration
          print(self.count)
          self.A = self.B
          self.B = self.count


c = Fibonaci(0,1,34)
for i in c:
    print(i)


