def on_button_pressed_a():
    PLAYER.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    PLAYER.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def generate_wall():
    sprite: game.LedSprite = None
    sprite = game.create_sprite(randint(0, 5), 0)
    sprite.set_direction(180)
    return sprite

def generate_walls(n):
    walls_list: List[game.LedSprite] = []
    for i in range(n):
        walls_list.push(generate_wall())
    return walls_list

def move_walls(wall_list: List[game.LedSprite], delay: int):
    for i in range(4):
        pause(delay)
        for item in wall_list:
            item.move(1)

def delete_walls(missed_walls: List[game.LedSprite]):
    for missed_wall in missed_walls:
        missed_wall.delete()

SCORE = 0
PLAYER = game.create_sprite(2, 4)
SPEED = 250
DIFFICULTY = 1

while not (game.is_game_over()):
    walls = generate_walls(DIFFICULTY)
    move_walls(walls, SPEED)

    for wall in walls:
        if PLAYER.is_touching(wall):
            game.add_score(SCORE)
            game.game_over()

    delete_walls(walls)

    SCORE += DIFFICULTY

    if SPEED > 50:
        SPEED -= 5

