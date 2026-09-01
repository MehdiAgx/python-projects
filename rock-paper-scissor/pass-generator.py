#1 variables and imports and modules

from abc import ABC,abstractmethod
import random
import string

#2 create pass generator abstract class

class PasswordGeneratorAbstract(ABC):
    @abstractmethod
    def generate_password(self, length=15):
        pass



#3  create numeric pass generator   

class NumericPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.digits

    def generate_password(self, length=15):
        return ''.join(str(random.choice(self.letters)) for _ in range(length))

#4  create letter pass generator   

class LetterPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.ascii_letters

    def generate_password(self, length=10):
        return ''.join(str(random.choice(self.letters)) for _ in range(length))

#5   create mix pass generator   

class MixedPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.ascii_letters + string.digits

    def generate_password(self, length=10):
        return ''.join(str(random.choice(self.letters)) for _ in range(length))


#6  run

generator = MixedPasswordGenerator()


print(generator.generate_password())