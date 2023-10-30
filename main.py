import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = []




class Balle:
    def __init__(self, x, y, change_x, change_y, rayon, couleur):
        self.x = x
        self.y = y
        self.change_x = random.randint(-10, 10)
        self.change_y = random.randint(-10, 10)
        self.rayon = rayon
        self.couleur = couleur
    def update(self):
        self.x +=self.change_x
        self.y += self.change_y

        if self.x < 0:
            self.change_x -= 2*self.change_x
        elif self.y < 0:
            self.change_y -= 2*self.change_y
        elif self.x > SCREEN_WIDTH:
            self.change_x -= 2 * self.change_x
        elif self.y > SCREEN_HEIGHT:
            self.change_y -= 2*self.change_y


    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.couleur)

class Rectangle:
    def __init__(self, x, y, width, height,couleur, tilt_angle):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.change_x = random.randint(-10, 10)
        self.change_y = random.randint(-10, 10)
        self.tilt_angle = tilt_angle
        self.couleur = couleur

    def update(self):
        self.x +=self.change_x
        self.y += self.change_y

        if self.x < 0:
            self.change_x -= 2*self.change_x
        elif self.y < 0:
            self.change_y -= 2*self.change_y
        elif self.x > SCREEN_WIDTH:
            self.change_x -= 2 * self.change_x
        elif self.y > SCREEN_HEIGHT:
            self.change_y -= 2*self.change_y


    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.couleur, self.tilt_angle)

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_de_balles = []
        self.liste_de_rectangle = []
        pass

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
        pass

    def on_draw(self):
        arcade.start_render()
        for i in self.liste_de_balles:
            i.draw()
        for i in self.liste_de_rectangle:
            i.draw()

    def update(self, delta_time):
        for i in self.liste_de_balles:
            i.update()

        for i in self.liste_de_rectangle:
            i.update()

    def on_mouse_press(self, x, y, button, modifiers):

        if button == arcade.MOUSE_BUTTON_LEFT:
            #for i in range(5):
                ma_balle = Balle(x, y, 5, 10, 15, arcade.color.WHITE)
                self.liste_de_balles.append(ma_balle)

        if button == arcade.MOUSE_BUTTON_RIGHT:
            #for i in range(5):
                mon_rectangle = Rectangle(x, y, 25, 25, arcade.color.WHITE, 0)
                self.liste_de_rectangle.append(mon_rectangle)

def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()

if __name__ == '__main__':
    main()
