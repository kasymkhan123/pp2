import pygame

# DEFENSE: I moved UI functions to a separate file to keep main.py clean.
# This follows the DRY principle (Don't Repeat Yourself).

def draw_text(surface, text, font, color, x, y):
    """Simple helper to draw text on the screen."""
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, (x, y))

def draw_button(surface, rect, text, font, bg_color, text_color):
    """Draws a rectangular button and centers the text inside it."""
    pygame.draw.rect(surface, bg_color, rect)
    text_obj = font.render(text, True, text_color)
    
    # EXPLANATION: get_rect(center=...) automatically centers the text inside the button area.
    text_rect = text_obj.get_rect(center=rect.center)
    surface.blit(text_obj, text_rect)