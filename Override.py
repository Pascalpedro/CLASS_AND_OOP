Class Animal:
    def __init__(self, can_fly=False):
        self.can_fly = can_fly
    def fly(self):
        if self.can_fly:
            print("I CAN FLY!")
        else:
            print("I CAN NOT FLY!")
            
 Class Bird:
      def fly(self):
          print("i am flying high!!")
        
 bird = Bird()
bird.fly()     #I am flying high....
