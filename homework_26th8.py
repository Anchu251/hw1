#1.SHOP , Hàm đếm sô len()
from ast import Return

print('BÀI 1: SHOP')
class Shop:
    def __init__(self, name, item):
        self.name = name
        self.item = item
    def get_items_count(self):
        return len(self.item)
shop=Shop('My shop', ['coconuts', 'bananas', 'peaches'])
number_of_items = shop.get_items_count()
print(shop.get_items_count())


#2.HERO
print ('\nBAI 2: HERO')
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
           self.health = 0
           print(f'{self.name} was defeated')
    def heal(self, amount):
        self.health += amount
hero = Hero("ANCHUU", 200)
print(hero.defend(70))
hero.heal(30)
print(hero.defend(159))
print(hero.defend(1))


#EMPLOYEE 
print ('\nBAI3: EMPLOYEE')
class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    def get_annual_salary(self):
        return self.salary * 12
    def raise_salary(self, amount):
        self.salary += amount
        return self.salary
employee = Employee(23011033, "Anchuu", "Meo", 2500)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())


#CUP: 
print('\nBAI 4 : CUP')
class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity
    def fill(self, milliliters):
        if self.quantity + milliliters <= self.size:
           self.quantity += milliliters
    def status(self):
        return self.size - self.quantity
cup = Cup(100,50)
print(cup.status())
cup.fill(10)
cup.fill(30)
print(cup.status())
cup.fill(100)
print(cup.status())

#FLOWER 
print('\nBAI 5: FLOWER')
class Flower:
    def __init__ (self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False
    def water(self, quantity):
        if quantity >= self.water_requirements:
            self.is_happy = True
    def status(self):
        if self.is_happy:
            return f'{self.name} is happy'
        else:
            return f'{self.name} is not happy'
flower = Flower("apple meomeo", 50)
flower.water(30)
print(flower.status())
flower.water(30)
print(flower.status())
flower.water(60)
print(flower.status())

#STEAM USER  Append() : thêm một phần tử vào dsach (game là list nên ko dùng add() được)
print('\nBAI 6: STEAM USER')
class SteamUser:
    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0
    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return f'{self.username} is playing {game}'
        else:
            return f'{game} is not in library'
    def buy_game(self, game):
        if game not in self.games: 
            self.games.append(game)
            return f'{self.username} bought {game}'
        else:
            return f'{game} is already in your library'
    def status(self):
        game_count = len(self.games)
        return f'{self.username} has {game_count} games. Total play time: {self.played_hours}'
user = SteamUser('Meomeo', ['Rainbow Six Siege', 'CS:GO', 'Fortnite'])
print(user.play('Fortnite',3))
print(user.play('Oxygen not Included',5))
print(user.buy_game('CS:GO'))
print(user.buy_game('Oxygen not Included'))
print(user.play('Oxygen not Included',6))
print(user.status())

#PROGRAMMER
print('\n BÀI 7: PROGRAMMER')
class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills
    def watch_course(self, course_name, language, skills_earned):
        if self.language  == language:
            self.skills += skills_earned
            return f'{self.name} watched {course_name}'
        else:
            return f'{self.name} does not know {language}'
    def change_language(self, new_language, skills_needed):
        if self.skills >= skills_needed:
            if self.language == self.language:
                return f'{self.name} already knows {new_language}'
            else:
                previous_language = self.language
                self.language = new_language
                return f'{self.name} switched from {previous_language} to {new_language}'
        else:
            needed_skills = skills_needed - self.skills
            return f'{self.name} needs {needed_skills} more skills'
programmer = Programmer('John', 'Java', 50)
print(programmer.watch_course('Python Mastercllass', 'Python', 84))
print(programmer.change_language('Java', 30))
print(programmer.change_language('Python',100))
print(programmer.watch_course('Java: zero to hero', 'Java', 50))
print(programmer.change_language('Python', 100))
print(programmer.watch_course('Python Masterclass', 'Pỵthon', 84))

    



    