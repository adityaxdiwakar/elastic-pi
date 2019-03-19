import time
import sys

class Block:
    def __init__(self, width, x, mass, velocity):
        self.x = x
        self.mass = mass
        self.velocity = velocity 
        self.width = width

    def left(self):
        return self.x - (self.width/2)

    def right(self):
        return self.x + (self.width/2)

    def move(self):
        self.x += self.velocity

    def is_wall_hit(self):
        if self.x <= 0:
            return True
        return False

    def reverse(self):
        self.velocity *= -1
    
    def has_collision(self, other):
        #print(f"Master left: {self.left()} and counter right: {other.right()}")
        if other.right() >= self.left():
            return True
        return False

    def collide_velocity(self, other):
        diff_mass = self.mass - other.mass
        sum_mass = self.mass + other.mass
        vel_half_1 = (diff_mass/sum_mass) * self.velocity
        vel_half_2 = (2*other.mass/sum_mass) * other.velocity
        self.velocity = vel_half_1 + vel_half_2

mass = 100 ** (int(sys.argv[1])-1)

master_block = Block(100, 1000, mass, -5)
counter_block = Block(50, 100, 1, 0)

start = time.time()
counter = 0
last_hit = time.time()
while True:
    master_block.move()
    counter_block.move()
    if master_block.has_collision(counter_block):
        master_block.collide_velocity(counter_block)
        counter_block.collide_velocity(master_block)
        counter += 1   
        last_hit = time.time()

    if counter_block.is_wall_hit():
        counter_block.reverse()
        counter += 1   
        last_hit = time.time()

    if time.time() > last_hit + 0.25:
        break

print(f"{int(sys.argv[1])} generated: {counter/(10**(int(sys.argv[1])-1))} and took {int((time.time() - start)*1000)}ms.")