import pygame
import datetime
import tools 

def main():
    pygame.init()
    
    # Window setup
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Paint - TSIS 2')
    clock = pygame.time.Clock()

    # Drawing canvas (keeps the actual artwork)
    canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    canvas.fill(tools.WHITE)

    pygame.font.init()
    font = pygame.font.SysFont("Arial", 20)

    # Default states
    active_color = tools.BLACK
    active_tool = 'pencil' 
    brush_size = 5 

    prev_mouse_pos = None 
    shape_start_pos = None 
    
    is_typing_text = False
    current_text = ""
    text_position = (0, 0)

    while True:
        keys_pressed = pygame.key.get_pressed()
        ctrl_held = keys_pressed[pygame.K_LCTRL] or keys_pressed[pygame.K_RCTRL]
        is_mouse_pressed = pygame.mouse.get_pressed()[0]
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if is_typing_text:
                        is_typing_text = False # Cancel text input
                        current_text = ""
                    else:
                        return
                
                # Save canvas on Ctrl+S
                if event.key == pygame.K_s and ctrl_held:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    filename = f"canvas_{timestamp}.png"
                    
                    # Crop the canvas to avoid saving the UI menus
                    drawing_area = pygame.Rect(0, tools.TOOLBAR_HEIGHT, SCREEN_WIDTH - 80, SCREEN_HEIGHT - tools.TOOLBAR_HEIGHT)
                    sub_surface = canvas.subsurface(drawing_area)
                    pygame.image.save(sub_surface, filename)
                    print(f"Saved: {filename}")

                # Change brush size using number keys
                if not is_typing_text:
                    if event.key == pygame.K_1: brush_size = 2  
                    if event.key == pygame.K_2: brush_size = 5  
                    if event.key == pygame.K_3: brush_size = 10 
                
                # Text typing logic
                if is_typing_text:
                    if event.key == pygame.K_RETURN:
                        # Render and stamp the text onto the canvas
                        text_surface = font.render(current_text, True, active_color)
                        canvas.blit(text_surface, text_position)
                        is_typing_text = False
                        current_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        current_text = current_text[:-1]
                    else:
                        current_text += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    # 1. Clicked on the top toolbar (Tool selection)
                    if mouse_y < tools.TOOLBAR_HEIGHT:
                        tool_index = mouse_x // tools.BUTTON_WIDTH
                        if tool_index < len(tools.TOOL_NAMES):
                            active_tool = tools.TOOL_NAMES[tool_index]
                            is_typing_text = False # Reset text tool if changed
                    
                    # 2. Clicked on the right panel (Color palette)
                    elif mouse_x > SCREEN_WIDTH - 80:
                        if 100 <= mouse_y <= 130: active_color = tools.RED
                        elif 150 <= mouse_y <= 180: active_color = tools.GREEN
                        elif 200 <= mouse_y <= 230: active_color = tools.BLUE
                        elif 250 <= mouse_y <= 280: active_color = tools.BLACK
                        elif 300 <= mouse_y <= 310: active_color = tools.YELLOW
                    
                    # 3. Clicked on the drawing canvas
                    elif mouse_x < SCREEN_WIDTH - 80 and mouse_y > tools.TOOLBAR_HEIGHT:
                        shape_start_pos = (mouse_x, mouse_y)
                        prev_mouse_pos = (mouse_x, mouse_y)
                        
                        if active_tool == 'fill':
                            tools.flood_fill(canvas, mouse_x, mouse_y, active_color)
                            
                        elif active_tool == 'text':
                            is_typing_text = True
                            text_position = (mouse_x, mouse_y)
                            current_text = ""

            # Mouse button released
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if shape_start_pos and active_tool in ['line', 'rect', 'circle', 'triangle']:
                    if mouse_x < SCREEN_WIDTH - 80 and mouse_y > tools.TOOLBAR_HEIGHT:
                        start_x, start_y = shape_start_pos
                        
                        if active_tool == 'line':
                            pygame.draw.line(canvas, active_color, shape_start_pos, (mouse_x, mouse_y), brush_size)
                        elif active_tool == 'rect':
                            rect_w = mouse_x - start_x
                            rect_h = mouse_y - start_y
                            pygame.draw.rect(canvas, active_color, (start_x, start_y, rect_w, rect_h), brush_size)
                        elif active_tool == 'circle':
                            radius = int(((mouse_x - start_x)**2 + (mouse_y - start_y)**2)**0.5)
                            pygame.draw.circle(canvas, active_color, shape_start_pos, radius, brush_size)
                        elif active_tool == 'triangle':
                            point2 = (mouse_x, mouse_y)
                            point3 = (start_x - (mouse_x - start_x), mouse_y)
                            pygame.draw.polygon(canvas, active_color, [shape_start_pos, point2, point3], brush_size)
                
                prev_mouse_pos = None
                shape_start_pos = None

            # Mouse movement (drawing with pencil/eraser)
            if event.type == pygame.MOUSEMOTION:
                if is_mouse_pressed and mouse_x < SCREEN_WIDTH - 80 and mouse_y > tools.TOOLBAR_HEIGHT:
                    if active_tool in ['pencil', 'eraser']:
                        draw_color = tools.WHITE if active_tool == 'eraser' else active_color
                        if prev_mouse_pos is not None:
                            pygame.draw.line(canvas, draw_color, prev_mouse_pos, (mouse_x, mouse_y), brush_size * 2)
                            pygame.draw.circle(canvas, draw_color, (mouse_x, mouse_y), brush_size)
                        prev_mouse_pos = (mouse_x, mouse_y)

        # Rendering
        screen.blit(canvas, (0, 0)) # Draw the saved canvas first
        
        # Live preview for shapes while dragging the mouse
        if is_mouse_pressed and shape_start_pos and active_tool in ['line', 'rect', 'circle', 'triangle']:
            start_x, start_y = shape_start_pos
            if active_tool == 'line':
                pygame.draw.line(screen, active_color, shape_start_pos, (mouse_x, mouse_y), brush_size)
            elif active_tool == 'rect':
                rect_w = mouse_x - start_x
                rect_h = mouse_y - start_y
                pygame.draw.rect(screen, active_color, (start_x, start_y, rect_w, rect_h), brush_size)
            elif active_tool == 'circle':
                radius = int(((mouse_x - start_x)**2 + (mouse_y - start_y)**2)**0.5)
                pygame.draw.circle(screen, active_color, shape_start_pos, radius, brush_size)
            elif active_tool == 'triangle':
                point2 = (mouse_x, mouse_y)
                point3 = (start_x - (mouse_x - start_x), mouse_y)
                pygame.draw.polygon(screen, active_color, [shape_start_pos, point2, point3], brush_size)

        # Live preview for text input
        if is_typing_text:
            preview_text = font.render(current_text + "|", True, active_color)
            screen.blit(preview_text, text_position)

        # Draw the UI on top of everything
        tools.draw_ui(screen, SCREEN_WIDTH, SCREEN_HEIGHT, active_tool, brush_size, font)
        
        pygame.display.flip()
        clock.tick(120)

if __name__ == '__main__':
    main()