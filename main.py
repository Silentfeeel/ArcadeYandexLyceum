import arcade

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Перемещение круга"

# Скорость перемещения
MOVEMENT_SPEED = 50


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        # Начальная позиция круга
        self.circle_x = width // 2
        self.circle_y = height // 2
        self.circle_radius = 30

        # Цвет круга
        self.circle_color = arcade.color.BLUE

    def on_draw(self):
        self.clear()
        # Рисуем круг
        arcade.draw_circle_filled(self.circle_x, self.circle_y, self.circle_radius, self.circle_color)

    def on_key_press(self, key, modifiers):
        """Обрабатывает нажатия клавиш"""
        if key == arcade.key.W:  # Вверх
            self.circle_y += MOVEMENT_SPEED
        elif key == arcade.key.S:  # Вниз
            self.circle_y -= MOVEMENT_SPEED
        elif key == arcade.key.A:  # Влево
            self.circle_x -= MOVEMENT_SPEED
        elif key == arcade.key.D:  # Вправо
            self.circle_x += MOVEMENT_SPEED

        # Проверяем границы экрана
        self.circle_x = max(self.circle_radius, min(self.circle_x, SCREEN_WIDTH - self.circle_radius))
        self.circle_y = max(self.circle_radius, min(self.circle_y, SCREEN_HEIGHT - self.circle_radius))


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()