import random
class Game:
    enemy = "name"
    turn = 1
    health = 100
    #armor = 100
    damage = 10
    enemyhp = 1
    enemydmg = 1
    critchance = 20
    enemyMax = 1
    healthBar = ""
    slash = False
    pierce = False
    blunt = False


    def __init__(self, enemy, health, damage):
        self.enemy = enemy
        self.enemyhp = health
        self.enemydmg = damage
        self.enemyMax = self.enemyhp
        self.healthBar = "[{}/{}]".format(self.enemyhp, self.enemyMax)
        #print(self.healthBar) #Enemy heath bar check
        #print(self.enemyMax) #Checks to see if max hp is set correctly

    def fight(self):
        crit = random.randint(1,self.critchance)
        if crit == 10:
            self.damage = self.damage*2
            #print(self.enemyhp) #Checks to see if enemy has right amount of hp
            print(("You CRIT the {}{} for {} damage").format(self.enemy, self.healthBar, self.damage))
        else:
            #self.damage = random.randint(7,13)
            #print(self.enemyhp) #Checks to see if enemy has right amount of hp
            print(("You hit the {} {} for {} damage").format(self.enemy, self.healthBar, self.damage))
        

    def enemyFight(self):
        crit = random.randint(1,40)
        if crit == 20:
            totaldamage = random.randint((self.enemydmg - 3) * 2, (self.enemydmg + 3) * 2)
            #print(totaldamage)
            print("The {}{} CRITS you for {} damage".format(self.enemy, self.healthBar, totaldamage))
        else:
            totaldamage = random.randint(self.enemydmg - 3, self.enemydmg + 3)
            #print(totaldamage)
            print("You get hit for {} by the {}".format(totaldamage, self.enemy))
        if self.health - totaldamage < 0:
            totaldamage = self.health
        self.health -= totaldamage
    
    def slasha(self):
        self.slash = True
        self.piece = False
        self.blunt = False
        self.damage = random.randint(7,13)
        
    
    def piercea(self):
        self.slash = False
        self.pierce = True
        self.blunt = False
        self.damage = random.randint(7,13)
        
    
    def blunta(self):
        self.slash = False
        self.piece = False
        self.blunt = True
        self.damage = random.randint(7,13)
        
    
    def heal(self):
        if self.health + 10 <= 100:
            print("You heal yourself")
            self.health += 10
        else:
            print("You are already at full hp")

    def die(self):
        print("You have slain the {}".format(self.enemy))
        
    def getHp(self):
        return "You are at {}% Health".format(self.health)
    
    def setHp(self, number):
        self.hp = number

    def getArmor(self):
        return "You are at {}% Armor".format(self.armor)

    def setArmor(self, number):
        self.armor = number
    
    def getTurn(self):
        return "You are on turn {}".format(self.turn)

    def setEnemy(self, name):
        self.enemy = name
    
    def damageCheck(self):
        if self.enemy == "Slime":
            if self.pierce == True:
                self.damage = int(self.damage / 2)
                print("Your attack wasn't very effective...")
            elif self.blunt == True:
                self.damage = self.damage * 2
                print("Your attack was very effective!")
            else:
                pass
        if self.enemyhp - self.damage < 0:
            self.damage = self.enemyhp
        self.enemyhp -= self.damage
    
    def update(self):
        self.healthBar = "[{}/{}]".format(self.enemyhp, self.enemyMax)

    
#Start of the Game
number = random.randint(1,4)
#Encounters
if number == 1:
    encounter = "Slime"
    health = 50
    damage = 10
elif number == 2:
    encounter = "Skeleton"
    health = 100
    damage = 25
else:
    encounter = "Ogre"
    health = 200
    damage = 20
Game = Game(encounter, health, damage)
print("You encounter a(n) {}{}!".format(Game.enemy, Game.healthBar))

#Choices and combat, constantly loops until Game wins or loses
while True:
    choice = int(input("""What do you want to do:
                        1) Attack [7 - 13 damage]
                        2) Defend
                        3) Heal [10 Health]
                        4) Escape
                        -> """))
    if choice == 1:
        choice2 = int(input("""
                            1)Slash
                            2)Pierce
                            3)Blunt
                            -> """))
        if choice2 == 1:
            Game.slasha()
        if choice2 == 2:
            Game.piercea()
            print(Game.pierce)
        else:
            Game.blunta()
        Game.fight()
        Game.damageCheck()
        Game.enemyFight()
        print(Game.getHp())
    elif choice == 2:
        pass
    elif choice == 3:
        Game.heal()
        Game.enemyFight()
        print(Game.getHp())
    elif choice == 4:
        if Game.enemy != "Skeleton":
            print("You successfully escape...")
            break
        else:
            print("You try to run but the skeleton shoots you in the back and kills you instantly lmao")
            Game.health = 0
    else:
        print("Closing game...")
        break


    if Game.enemyhp == 0:
        Game.die()
        break
    if Game.health <= 0:
        break    
    else:
        pass
    Game.update()
    Game.turn += 1

if Game.health > 0:
    print("Congrats you win this portion of the game!")
else:
    num = random.randint(1,5)
    if num == 1:
        print("You played yoruself...")
    elif num == 2:
        print("You died a miserable death...")
    elif num == 3:
        print("You let out your last breathe...")
    elif num == 4:
        print("The grasp of death squeezes you...")
    else:
        print("You fade to black...")
