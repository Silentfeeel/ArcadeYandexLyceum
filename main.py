import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Перемещение круга"

# Скорость перемещения
MOVEMENT_SPEED = 50


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.PINK)

        # Начальная позиция круга босса
        self.circle_x = width // 2
        self.circle_y = height // 2
        self.circle_radius = 30

        # Начальная позиция круга игрока
        self.circle_radius1 = 30
        self.circle_x1 = width - self.circle_radius
        self.circle_y1 = height - self.circle_radius


    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.circle_x, self.circle_y, self.circle_radius + 53, arcade.color.BLACK)

        arcade.draw_circle_filled(self.circle_x, self.circle_y, self.circle_radius + 50, arcade.color.RED)
        arcade.draw_circle_filled(self.circle_x, self.circle_y, self.circle_radius + 3, arcade.color.BLACK)

        arcade.draw_circle_filled(self.circle_x, self.circle_y, self.circle_radius, arcade.color.WHITE)

        arcade.draw_circle_filled(self.circle_x1, self.circle_y1, self.circle_radius1, arcade.color.WHITE)
        arcade.draw_circle_filled(self.circle_x, self.circle_y, self.circle_radius - 19, arcade.color.BLACK)


    def on_key_press(self, key, modifiers):
        """Обрабатывает нажатия клавиш"""
        if key == arcade.key.W:  # Вверх
            self.circle_y1 += MOVEMENT_SPEED
        elif key == arcade.key.S:  # Вниз
            self.circle_y1 -= MOVEMENT_SPEED
        elif key == arcade.key.A:  # Влево
            self.circle_x1 -= MOVEMENT_SPEED
        elif key == arcade.key.D:  # Вправо
            self.circle_x1 += MOVEMENT_SPEED

        # Проверяем границы экрана
        self.circle_x1 = max(self.circle_radius1, min(self.circle_x1, SCREEN_WIDTH - self.circle_radius1))
        self.circle_y1 = max(self.circle_radius1, min(self.circle_y1, SCREEN_HEIGHT - self.circle_radius1))


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()