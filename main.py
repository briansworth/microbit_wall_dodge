def generate_walls(n):
    walls_list: List[game.LedSprite] = []
    for i in range(n):
        walls_list.append(generate_wall())
    return walls_list

def generate_wall():
    sprite = game.create_sprite(randint(0, 5), 0)
    sprite.set_direction(180)
    return sprite

def delete_walls(walls: List[game.LedSprite]):
    for wall in walls:
        wall.delete()

def move_walls(walls: List[game.LedSprite], delay: int):
    for i in range(4):
        pause(delay)
        for wall in walls:
            wall.move(1)

def is_gameover(player: game.LedSprite, walls: list[game.LedSprite]):
    for wall in walls:
        if player.is_touching(wall):
            return True
    return False

def on_button_pressed_a():
    PLAYER.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    PLAYER.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

DIFFICULTY = 2
SPEED = 250

SCORE = 0
PLAYER = game.create_sprite(2, 4)

while not (game.is_game_over()):
    walls = generate_walls(DIFFICULTY)
    move_walls(walls, SPEED)

    if is_gameover(PLAYER, walls):
        game.add_score(SCORE)
        game.game_over()
    delete_walls(walls)

    SCORE += DIFFICULTY
    if SPEED > 50:
        SPEED -= 5
