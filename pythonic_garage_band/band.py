from abc import ABC, abstractmethod


class Musician:
   
    #Initializes a Musician object with a name attribute.
   def __init__(self,name):
      self.name = name

    #An abstract method that returns a string representation of a Musician object.
   @abstractmethod
   def __str__(self):
      pass

    #An abstract method that returns a string representation of a Musician object.
   @abstractmethod
   def __reper__(self):
      pass

    #An abstract method that returns a string representation of the instrument a Musician object plays.
   @abstractmethod
   def get_instrument(self):
      pass

    #An abstract method that returns a string representation of the solo a Musician object plays.
   @abstractmethod
   def play_solo(self):
      pass
   
##############################################################################################################
class Guitarist(Musician):

    #Initializes a Guitarist object with a name attribute and calls the init method of the parent class, Musician.
    def __init__(self,name):
        super().__init__(name)

    #Returns a string representation of a Guitarist object.
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    
    #Returns a string representation of a Guitarist object.
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    
    #Returns a string representation of the instrument a Guitarist object plays.
    def get_instrument(self):
        return "guitar"
    
    #Returns a string representation of the solo a Guitarist object plays.
    def play_solo(self):
        return "face melting guitar solo"
################################################################################################################################   
class Bassist(Musician):

    #Initializes a Bassist object with a name attribute and calls the init method of the parent class, Musician.
    def __init__(self,name):
        super().__init__(name)

    #Returns a string representation of a Bassist object.
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    
    #Returns a string representation of a Bassist object.
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    
    #Returns a string representation of the instrument a Bassist object plays.
    def get_instrument(self):
        return "bass"
    
    #Returns a string representation of the solo a Bassist object plays.
    def play_solo(self):
        return "bom bom buh bom"   
###############################################################################################################################   
class Drummer(Musician):

    #Initializes a Drummer object with a name attribute and calls the init method of the parent class, Musician.
    def __init__(self,name):
        super().__init__(name)

    #Returns a string representation of a Drummer object.
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    
    #Returns a string representation of a Drummer object.
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    
    #Returns a string representation of the instrument a Drummer object plays.
    def get_instrument(self):
        return "drums"
    
    #Returns a string representation of the solo a Drummer object plays.
    def play_solo(self):
        return "rattle boom crash"

##########################################################################################################################################
class Band:

   instances = []

   #Initializes a Band object with a name attribute and a list of members attribute and appends it to the instances list.
   def __init__(self, name, members):
        self.name= name
        self.members = members
        Band.instances.append(self)        

    #Returns a list of string representations of each member's solo played in the band.
   def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())

        return solos

    #Returns a string representation of a Band object.
   def __str__(self):
        return f'the band name is : {self.name}'

    #Returns a string representation of a Band object.
   def __repr__(self):
        return f'the band name is : {self.name} and it`s the best ;)'
    
   
    #A class method that returns the instances list of all Band objects created.
   @classmethod
   def to_list(cls):
        return cls.instances 