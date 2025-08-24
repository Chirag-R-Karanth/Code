import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# -----------------------
# Setup basic parameters
# -----------------------
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎯 Guess the Number Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE  = (70, 130, 180)
RED   = (255, 60, 60)
GREEN = (34, 139, 34)

# Fonts
FONT = pygame.font.SysFont(None, 40)
BIG_FONT = pygame.font.SysFont(None, 60)

# Game state variables
secret_number = random.randint(1, 100)
attempts = 0
user_input = ''
message = "Guess a number between 1 and 100"

# -----------------------
# Utility: Render Text
# -----------------------
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# -----------------------
# Main Game Loop
# -----------------------
running = True
while running:
    screen.fill(WHITE)  # Clear screen each frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle keyboard input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                try:
                    guess = int(user_input)
                    attempts += 1

                    if guess < secret_number:
                        message = "🔻 Too low!"
                    elif guess > secret_number:
                        message = "🔺 Too high!"
                    else:
                        message = f"✅ Correct! {secret_number} in {attempts} tries!"
                        # Reset after correct guess
                        secret_number = random.randint(1, 100)
                        attempts = 0

                    user_input = ''  # Clear after submission
                except ValueError:
                    message = "❌ Invalid number!"
                    user_input = ''

            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.unicode.isdigit():
                user_input += event.unicode

    # -----------------------
    # Draw UI
    # -----------------------
    draw_text("🎮 Guess the Number", BIG_FONT, BLUE, 120, 30)
    draw_text("Your Guess: " + user_input, FONT, BLACK, 160, 120)
    draw_text(message, FONT, GREEN if "Correct" in message else RED, 100, 200)
    draw_text("Press Enter to submit", FONT, BLACK, 160, 320)

    pygame.display.flip()  # Update screen

pygame.quit()
sys.exit()
