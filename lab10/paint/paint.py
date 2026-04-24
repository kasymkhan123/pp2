import pygame

main_screen_width  = 640
main_screen_height = 480
main_screen_sizes = (main_screen_width, main_screen_height)

icon_shape_height    = 50
icon_rectangle_start = 0
icon_rectangle_end   = 50
icon_line_start      = 50
icon_line_end        = 100
icon_circle_start    = 100
icon_circle_end      = 150
icon_triangle_start  = 150
icon_triangle_end    = 200
icon_eraser_start    = 200
icon_eraser_end      = 250

icon_color_width   = 80
icom_color_height  = 30
icon_color_red_x   = 560
icon_color_red_y   = 100
icon_color_blue_x  = 560
icon_color_blue_y  = 150
icon_color_green_x = 560
icon_color_green_y = 200

tab_color       = (100, 100, 100)
right_tab_color = (50, 50, 50)
rect_color      = (180, 0, 180)
line_color      = (170, 0, 120)
circle_color    = (120, 0, 120)
triangle_color  = (80, 0, 80)

white = (255, 255, 255)
black = (0, 0, 0)
red   = (255, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)

shape_triangle = 'TRIANGLE'
shape_square = 'SQUARE'
shape_circle = 'CIRCLE'

color_chosen = black
shape_chosen = shape_square

def drawMainIcons(mainscreen):
    # Draw top menu
    pygame.draw.rect(mainscreen, tab_color, pygame.Rect(0, 0, main_screen_width, 40))
    pygame.draw.rect(mainscreen, rect_color, pygame.Rect(icon_rectangle_start + 5, 5, 40, 30))
    pygame.draw.rect(mainscreen, line_color, pygame.Rect(icon_line_start + 5, 5, 40, 30))
    pygame.draw.rect(mainscreen, circle_color, pygame.Rect(icon_circle_start + 5, 5, 40, 30))
    pygame.draw.rect(mainscreen, triangle_color, pygame.Rect(icon_triangle_start + 5, 5, 40, 30))
    pygame.draw.rect(mainscreen, white, pygame.Rect(icon_eraser_start + 5, 5, 40, 30))
    
    # Icons on buttons
    pygame.draw.rect(mainscreen, white, pygame.Rect(icon_rectangle_start + 10, 10, 30, 20))
    pygame.draw.circle(mainscreen, white, (icon_circle_start + 25, 20), 10)
    pygame.draw.polygon(mainscreen, white, [(icon_triangle_start + 10, 30), (icon_triangle_end - 10,30), (175,10)])
    
    # Draw color palette
    pygame.draw.rect(mainscreen, right_tab_color, pygame.Rect(560, 0, 80, main_screen_height))
    pygame.draw.rect(mainscreen, red, pygame.Rect(icon_color_red_x, icon_color_red_y, icon_color_width, icom_color_height))
    pygame.draw.rect(mainscreen, green, pygame.Rect(icon_color_green_x, icon_color_green_y, icon_color_width, icom_color_height))
    pygame.draw.rect(mainscreen, blue, pygame.Rect(icon_color_blue_x, icon_color_blue_y, icon_color_width, icom_color_height))


def main():
    pygame.init()
    screen = pygame.display.set_mode(main_screen_sizes)
    pygame.display.set_caption('Paint')
    clock = pygame.time.Clock()

    # NEW: Create a separate canvas surface where drawings will remain
    canvas = pygame.Surface(main_screen_sizes)
    canvas.fill(white)

    radius = 5
    last_pos = None # Stores the previous mouse position for smooth line drawing

    is_rectangle_drawer = False
    is_triangle_drawer = False
    is_circle_drawer = False
    is_line_drawer = True
    is_eraser = False

    while True:
        global color_chosen, shape_chosen
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        mouse_pressed = pygame.mouse.get_pressed()[0]
        position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or (event.key == pygame.K_w and ctrl_held) or (event.key == pygame.K_F4 and alt_held):
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    # 1. Check click on the top menu (Tools)
                    if position[1] < icon_shape_height:
                        is_rectangle_drawer = is_circle_drawer = is_line_drawer = is_eraser = is_triangle_drawer = False
                        if position[0] < icon_rectangle_end:
                            is_rectangle_drawer = True
                        elif position[0] < icon_line_end:
                            is_line_drawer = True
                        elif position[0] < icon_circle_end:
                            is_circle_drawer = True
                        elif position[0] < icon_triangle_end:
                            is_triangle_drawer = True
                        elif position[0] < icon_eraser_end:
                            is_eraser = True

                    # 2. Check click on the color palette (Colors)
                    elif position[0] > 560:
                        if icon_color_red_y <= position[1] <= icon_color_red_y + icom_color_height:
                            color_chosen = red
                        elif icon_color_green_y <= position[1] <= icon_color_green_y + icom_color_height:
                            color_chosen = green
                        elif icon_color_blue_y <= position[1] <= icon_color_blue_y + icom_color_height:
                            color_chosen = blue

                    # 3. Draw Shapes on the canvas on click
                    elif position[0] < 560 and position[1] > icon_shape_height:
                        if is_triangle_drawer:
                            pygame.draw.polygon(canvas, color_chosen, [(position[0], position[1]-20), (position[0]-20, position[1]+20), (position[0]+20, position[1]+20)])
                        elif is_rectangle_drawer:
                            pygame.draw.rect(canvas, color_chosen, (position[0]-20, position[1]-20, 40, 40))
                        elif is_circle_drawer:
                            pygame.draw.circle(canvas, color_chosen, position, 20)
                        
                        last_pos = position # Start a new line

                elif event.button == 3: # Right click decreases thickness
                    radius = max(2, radius - 2)
                elif event.button == 4: # Scroll up (optional) increases thickness
                    radius += 2

            # If mouse button is released, break the line
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                last_pos = None

            # 4. Draw lines and Eraser logic
            if event.type == pygame.MOUSEMOTION:
                if mouse_pressed and position[0] < 560 and position[1] > icon_shape_height:
                    if is_line_drawer or is_eraser:
                        current_color = white if is_eraser else color_chosen
                        
                        if last_pos is not None:
                            # Draw a line from the previous point to the new one (to prevent "gaps" during fast movement)
                            pygame.draw.line(canvas, current_color, last_pos, position, radius * 2)
                        
                        # Circle smooths the line edges
                        pygame.draw.circle(canvas, current_color, position, radius)
                        last_pos = position

        # Rendering: first show the canvas, then overlay the menu on top
        screen.blit(canvas, (0, 0))
        drawMainIcons(screen)
        
        pygame.display.flip()
        clock.tick(120)

main()