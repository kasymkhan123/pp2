import pygame
import random
import time

# DEFENSE: Passing username, settings, and personal_best so the game knows who is playing.
def play_snake(dis, dis_width, dis_height, username, settings, personal_best):
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
    dark_red = (139, 0, 0) # Poison color
    gray = (100, 100, 100) # Obstacle color

    snake_color = tuple(settings.get("snake_color", [0, 0, 0]))
    show_grid = settings.get("grid", False)

    clock = pygame.time.Clock()
    snake_block = 10
    base_speed = 15
    snake_speed = base_speed

    font_style = pygame.font.SysFont("arial", 25)
    score_font = pygame.font.SysFont("comicsansms", 20)

    game_over = False
    game_close = False

    x1 = dis_width // 2
    y1 = dis_height // 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    score = 0
    level = 1
    foods_per_level = 3
    start_time = pygame.time.get_ticks()

    # Entities
    foodx = random.randrange(0, dis_width - snake_block, snake_block)
    foody = random.randrange(0, dis_height - snake_block, snake_block)
    
    poisonx = random.randrange(0, dis_width - snake_block, snake_block)
    poisony = random.randrange(0, dis_height - snake_block, snake_block)

    # DEFENSE: Power-up states tracked using pygame.time.get_ticks() (milliseconds)
    powerup = None # Dict containing x, y, type, spawn_time
    active_effect = None
    effect_start_time = 0
    shield_active = False
    
    obstacles = []

    def spawn_obstacles():
        """EXPLANATION: Generates static walls on level 3+. Avoids center so snake doesn't get trapped."""
        obstacles.clear()
        if level >= 3:
            for _ in range(level * 2): # More obstacles at higher levels
                ox = random.randrange(0, dis_width - snake_block, snake_block)
                oy = random.randrange(0, dis_height - snake_block, snake_block)
                # Don't spawn near starting position
                if abs(ox - dis_width//2) > 50 and abs(oy - dis_height//2) > 50:
                    obstacles.append((ox, oy))

    while not game_over:
        while game_close:
            # DEFENSE: If game is closed, we return score and level to main.py to save to DB.
            return score, level

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return score, level
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block; y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block; y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block; x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block; x1_change = 0

        # DEFENSE: Shield Logic for Walls. If shielded, teleport to the other side!
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            if shield_active:
                shield_active = False # Shield used
                if x1 >= dis_width: x1 = 0
                elif x1 < 0: x1 = dis_width - snake_block
                if y1 >= dis_height: y1 = 0
                elif y1 < 0: y1 = dis_height - snake_block
            else:
                game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(blue)
        
        # Draw Grid if enabled
        if show_grid:
            for x in range(0, dis_width, snake_block):
                pygame.draw.line(dis, (100, 150, 200), (x, 0), (x, dis_height))
            for y in range(0, dis_height, snake_block):
                pygame.draw.line(dis, (100, 150, 200), (0, y), (dis_width, y))

        # Draw Obstacles
        for obs in obstacles:
            pygame.draw.rect(dis, gray, [obs[0], obs[1], snake_block, snake_block])

        # Draw Food and Poison
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, dark_red, [poisonx, poisony, snake_block, snake_block])

        # DEFENSE: Power-up logic. Spawns randomly, disappears after 8 seconds.
        current_ticks = pygame.time.get_ticks()
        
        if powerup is None and random.randint(1, 100) == 1:
            p_type = random.choice(['speed', 'slow', 'shield'])
            powerup = {
                'x': random.randrange(0, dis_width - snake_block, snake_block),
                'y': random.randrange(0, dis_height - snake_block, snake_block),
                'type': p_type,
                'time': current_ticks
            }
        
        if powerup:
            if current_ticks - powerup['time'] > 8000: # 8 seconds to disappear
                powerup = None
            else:
                color = yellow if powerup['type'] == 'speed' else (0,255,255) if powerup['type'] == 'shield' else white
                pygame.draw.rect(dis, color, [powerup['x'], powerup['y'], snake_block, snake_block])

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Self-collision and obstacle collision
        for x in snake_List[:-1]:
            if x == snake_Head:
                if shield_active: shield_active = False
                else: game_close = True
                
        for obs in obstacles:
            if obs[0] == x1 and obs[1] == y1:
                if shield_active: shield_active = False
                else: game_close = True

        # Draw snake
        for i, x in enumerate(snake_List):
            color = snake_color
            if shield_active: color = (0, 255, 255) # Cyan if shielded
            pygame.draw.rect(dis, color, [x[0], x[1], snake_block, snake_block])

        # Eating Normal Food
        if x1 == foodx and y1 == foody:
            foodx = random.randrange(0, dis_width - snake_block, snake_block)
            foody = random.randrange(0, dis_height - snake_block, snake_block)
            Length_of_snake += 1
            score += 1
            if score % foods_per_level == 0:
                level += 1
                base_speed += 2
                spawn_obstacles()

        # EXPLANATION: Poison Food Logic. Decreases length by 2. If <= 0, you die.
        if x1 == poisonx and y1 == poisony:
            poisonx = random.randrange(0, dis_width - snake_block, snake_block)
            poisony = random.randrange(0, dis_height - snake_block, snake_block)
            Length_of_snake -= 2
            if Length_of_snake <= 0:
                game_close = True
            else:
                snake_List = snake_List[-Length_of_snake:] # Shorten list

        # Eating Powerup
        if powerup and x1 == powerup['x'] and y1 == powerup['y']:
            if powerup['type'] == 'shield':
                shield_active = True
            else:
                active_effect = powerup['type']
                effect_start_time = current_ticks
            powerup = None

        # Apply timed effects (Speed / Slow)
        snake_speed = base_speed
        if active_effect:
            if current_ticks - effect_start_time > 5000: # 5 seconds duration
                active_effect = None
            else:
                if active_effect == 'speed': snake_speed = base_speed + 10
                elif active_effect == 'slow': snake_speed = max(5, base_speed - 10)

        # HUD
        current_time = (current_ticks - start_time) // 1000
        dis.blit(score_font.render(f"Score: {score} | Best: {personal_best}", True, yellow), [0, 0])
        dis.blit(score_font.render(f"Level: {level} | Speed: {snake_speed}", True, white), [0, 25])
        
        if shield_active:
            dis.blit(score_font.render("SHIELD ACTIVE", True, (0, 255, 255)), [0, 50])

        pygame.display.update()
        clock.tick(snake_speed)

    return score, level