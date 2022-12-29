import os
import random

class Player:
    isAlive = True
    numCharges = 0
    isShielded = False
    isShooting = False
    def charge(self):
        self.numCharges += 1
    def shield(self):
        self.isShielded = True
    def shoot(self):
        if self.numCharges > 0:
            self.numCharges = max(self.numCharges - 1, 0)
            self.isShooting = True

turnNumber = 1
player = Player()
ai = Player()

print("""
Welcome to Charge/Defend/Shoot, this is a more advanced version of Rock/Paper/Sissors, your objective is to
defeat your opponent. Starting at 0 charges, each turn you have only 3 options, to charge in attack (You are
required to have 1 charge before shooting), to defend yourself from an incoming attack, or to shoot your opponent.
Both players only have 1 life, and shooting at the same time won't kill each other.
This game requires knowing what options your opponent open and what they are most likely to do, Good Luck!
""")

while player.isAlive and ai.isAlive:
    # Show player and computer charges
    print("You are at", player.numCharges, "charges.")
    print("Your opponent is at", ai.numCharges, "charges.")
    choice = int(input(("""What are you going to do:
                            1) Charge
                            2) Shield
                            3) Shoot
                        ~~> """)))
    
    # Clear console
    os.system('cls')

    # Players's choice
    if choice == 1:
        player.charge()
        print("You gather energy...")
    elif choice == 2:
        player.shield()
    elif choice == 3:
        player.shoot()
        if not player.isShooting:
            print("You do not have enough energy to shoot.")
    else:
        break
        
    # Computer's choice
    if turnNumber == 1:
        cchoice = 1
    else:
        if ai.numCharges == 0:
            cchoice = random.randint(1,2)
        else:
            cchoice = random.randint(2,3)
    
    if cchoice == 1:
        ai.charge()
        print("Your opponent gathers energy...")
    elif cchoice == 2:
        ai.shield()
    elif cchoice == 3:
        ai.shoot()
        if not ai.isShooting:
            print("Your oppoenent does not have enough energy to shoot")
    
    # Fighting phase
    
    if player.isShooting:
        print("You let out a blast of energy")
    if player.isShielded:
        print("You prepare you defenses..")
    if ai.isShooting:
        print("Your opponent lets out a blast of energy")
    if ai.isShielded:
        print("Your opponent prepares their defenses..")
    
    print()

    if player.isShooting:
        if ai.isShooting:
            print("The attacks collide in the air and disperse...")
        elif not ai.isShielded:
            print("You disintegrate your opponent")
            ai.isAlive = False
        else:
            print("Your attack was blocked!")
    else:
        if ai.isShooting == True:
            if player.isShielded == True:
                print("You block the attack")
            else:
                player.isAlive = False
        else:
            pass
    
    print()

    # Reset Values
    player.isShielded = False
    player.isShooting = False
    ai.isShielded = False
    ai.isShooting = False
    turnNumber += 1

if not player.isAlive and not ai.isAlive:
    print("Draw.")
elif not ai.isAlive:
    print("You annihilate your opponent")
    print("You win.")
elif not player.isAlive:
    print("You get fried to a crisp")
    print("You lose.")
else:
    print("cheater?")
    