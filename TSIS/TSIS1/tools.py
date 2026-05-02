import pygame

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
YELLOW = (255, 255, 0)
TOOLBAR_COLOR = (100, 100, 100)
PALETTE_COLOR = (50, 50, 50)

# --- UI Settings ---
TOOLBAR_HEIGHT = 50
TOOL_NAMES = ['pencil', 'line', 'rect', 'circle', 'triangle', 'eraser', 'fill', 'text']
BUTTON_WIDTH = 80

def draw_ui(screen, screen_width, screen_height, active_tool, brush_size, font):
    """Draws the user interface (top toolbar and right color palette)"""
    # Top toolbar
    pygame.draw.rect(screen, TOOLBAR_COLOR, pygame.Rect(0, 0, screen_width, TOOLBAR_HEIGHT))
    
    # Tool buttons
    for i, tool in enumerate(TOOL_NAMES):
        btn_rect = pygame.Rect(i * BUTTON_WIDTH, 0, BUTTON_WIDTH, TOOLBAR_HEIGHT)
        bg_color = (150, 150, 150) if active_tool == tool else TOOLBAR_COLOR
        pygame.draw.rect(screen, bg_color, btn_rect)
        pygame.draw.rect(screen, BLACK, btn_rect, 1) # Border
        
        text_surf = font.render(tool, True, WHITE)
        screen.blit(text_surf, (i * BUTTON_WIDTH + 10, 15))
    
    # Color palette (right side)
    palette_x = screen_width - 80
    pygame.draw.rect(screen, PALETTE_COLOR, pygame.Rect(palette_x, 0, 80, screen_height))
    pygame.draw.rect(screen, RED, pygame.Rect(palette_x + 10, 100, 60, 30))
    pygame.draw.rect(screen, GREEN, pygame.Rect(palette_x + 10, 150, 60, 30))
    pygame.draw.rect(screen, BLUE, pygame.Rect(palette_x + 10, 200, 60, 30))
    pygame.draw.rect(screen, BLACK, pygame.Rect(palette_x + 10, 250, 60, 30))
    pygame.draw.rect(screen, YELLOW, pygame.Rect(palette_x + 10, 300, 60, 30))
    
    # Brush size indicator
    size_text = font.render(f"Size: {brush_size}", True, WHITE)
    screen.blit(size_text, (palette_x + 5, 350))


def flood_fill(surface, x, y, fill_color):
    """Fills an enclosed area with a selected color using a stack"""
    target_color = surface.get_at((x, y))[:3]
    fill_color = fill_color[:3]
    
    if target_color == fill_color:
        return

    stack = [(x, y)]
    surface_width, surface_height = surface.get_size()
    
    while stack:
        cx, cy = stack.pop()
        
        # Prevent filling outside the canvas and onto the menus
        if cx < 0 or cx >= surface_width - 80 or cy < TOOLBAR_HEIGHT or cy >= surface_height:
            continue
            
        if surface.get_at((cx, cy))[:3] == target_color:
            surface.set_at((cx, cy), fill_color)
            # Add neighboring pixels to the stack
            stack.extend([(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)])