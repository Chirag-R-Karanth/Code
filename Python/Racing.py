import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
DARK_GREEN = (0, 100, 0)

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.max_speed = 5
        self.acceleration = 0.2
        self.friction = 0.05
        self.turn_speed = 3
        self.width = 20
        self.height = 10
        
    def update(self, keys):
        # Handle turning
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.speed > 0:
                self.angle -= self.turn_speed
            elif self.speed < 0:
                self.angle += self.turn_speed
                
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.speed > 0:
                self.angle += self.turn_speed
            elif self.speed < 0:
                self.angle -= self.turn_speed
        
        # Handle acceleration
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.speed = min(self.speed + self.acceleration, self.max_speed)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.speed = max(self.speed - self.acceleration, -self.max_speed/2)
        else:
            # Apply friction
            if self.speed > 0:
                self.speed = max(0, self.speed - self.friction)
            elif self.speed < 0:
                self.speed = min(0, self.speed + self.friction)
        
        # Update position
        angle_rad = math.radians(self.angle)
        self.x += self.speed * math.cos(angle_rad)
        self.y += self.speed * math.sin(angle_rad)
        
        # Keep car on screen
        self.x = max(10, min(SCREEN_WIDTH - 10, self.x))
        self.y = max(10, min(SCREEN_HEIGHT - 10, self.y))
    
    def draw(self, screen):
        # Create car points
        angle_rad = math.radians(self.angle)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        
        # Car body points (rectangle rotated)
        points = [
            (-self.width//2, -self.height//2),
            (self.width//2, -self.height//2),
            (self.width//2, self.height//2),
            (-self.width//2, self.height//2)
        ]
        
        # Rotate and translate points
        rotated_points = []
        for px, py in points:
            rx = px * cos_a - py * sin_a + self.x
            ry = px * sin_a + py * cos_a + self.y
            rotated_points.append((rx, ry))
        
        # Draw car body
        pygame.draw.polygon(screen, RED, rotated_points)
        
        # Draw car direction indicator
        front_x = self.x + (self.width//2 + 5) * cos_a
        front_y = self.y + (self.width//2 + 5) * sin_a
        pygame.draw.circle(screen, YELLOW, (int(front_x), int(front_y)), 3)

class Checkpoint:
    def __init__(self, x, y, width=80, height=20):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.passed = False
        self.rect = pygame.Rect(x - width//2, y - height//2, width, height)
    
    def draw(self, screen):
        color = GREEN if not self.passed else GRAY
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, WHITE, self.rect, 2)
    
    def check_collision(self, car):
        car_rect = pygame.Rect(car.x - 10, car.y - 5, 20, 10)
        return self.rect.colliderect(car_rect)

class RacingGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pygame Racing Game")
        self.clock = pygame.time.Clock()
        
        # Initialize game objects
        self.car = Car(100, 300)
        self.checkpoints = [
            Checkpoint(700, 150),
            Checkpoint(700, 450),
            Checkpoint(400, 500),
            Checkpoint(100, 450),
            Checkpoint(100, 150),
            Checkpoint(400, 100)
        ]
        
        self.current_checkpoint = 0
        self.lap = 1
        self.max_laps = 3
        self.start_time = pygame.time.get_ticks()
        self.game_finished = False
        self.final_time = 0
        
        # Font for UI
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
    def draw_track(self):
        # Fill background with grass color
        self.screen.fill(DARK_GREEN)
        
        # Draw track outline (simple oval)
        track_points = [
            (150, 150), (650, 150), (750, 200), (750, 400),
            (650, 450), (150, 450), (50, 400), (50, 200)
        ]
        
        # Draw track surface
        pygame.draw.polygon(self.screen, GRAY, track_points)
        
        # Draw track lines
        inner_points = [
            (200, 200), (600, 200), (700, 250), (700, 350),
            (600, 400), (200, 400), (100, 350), (100, 250)
        ]
        pygame.draw.polygon(self.screen, WHITE, inner_points, 3)
        pygame.draw.polygon(self.screen, WHITE, track_points, 3)
        
        # Draw start/finish line
        pygame.draw.line(self.screen, WHITE, (80, 280), (120, 320), 5)
        start_text = self.small_font.render("START", True, WHITE)
        self.screen.blit(start_text, (85, 250))
    
    def update_checkpoints(self):
        current_cp = self.checkpoints[self.current_checkpoint]
        
        if current_cp.check_collision(self.car) and not current_cp.passed:
            current_cp.passed = True
            self.current_checkpoint = (self.current_checkpoint + 1) % len(self.checkpoints)
            
            # Check if completed a lap
            if self.current_checkpoint == 0:
                self.lap += 1
                # Reset all checkpoints for next lap
                for cp in self.checkpoints:
                    cp.passed = False
                
                # Check if race is finished
                if self.lap > self.max_laps:
                    self.game_finished = True
                    self.final_time = (pygame.time.get_ticks() - self.start_time) / 1000
    
    def draw_ui(self):
        # Speed display
        speed_mph = int(abs(self.car.speed) * 10)
        speed_text = self.font.render(f"Speed: {speed_mph} mph", True, WHITE)
        self.screen.blit(speed_text, (10, 10))
        
        # Lap display
        lap_text = self.font.render(f"Lap: {min(self.lap, self.max_laps)}/{self.max_laps}", True, WHITE)
        self.screen.blit(lap_text, (10, 50))
        
        # Time display
        if not self.game_finished:
            current_time = (pygame.time.get_ticks() - self.start_time) / 1000
        else:
            current_time = self.final_time
            
        minutes = int(current_time // 60)
        seconds = int(current_time % 60)
        time_text = self.font.render(f"Time: {minutes}:{seconds:02d}", True, WHITE)
        self.screen.blit(time_text, (10, 90))
        
        # Controls
        controls = [
            "Controls:",
            "Arrow Keys or WASD to drive",
            "ESC to quit"
        ]
        for i, control in enumerate(controls):
            text = self.small_font.render(control, True, WHITE)
            self.screen.blit(text, (10, SCREEN_HEIGHT - 80 + i * 20))
        
        # Game finished message
        if self.game_finished:
            finish_text = self.font.render("RACE FINISHED!", True, YELLOW)
            text_rect = finish_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            pygame.draw.rect(self.screen, BLACK, text_rect.inflate(20, 20))
            self.screen.blit(finish_text, text_rect)
            
            final_time_text = self.font.render(f"Final Time: {int(self.final_time//60)}:{int(self.final_time%60):02d}", True, YELLOW)
            time_rect = final_time_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40))
            self.screen.blit(final_time_text, time_rect)
            
            restart_text = self.small_font.render("Press R to restart", True, WHITE)
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 80))
            self.screen.blit(restart_text, restart_rect)
    
    def reset_game(self):
        self.car = Car(100, 300)
        self.checkpoints = [
            Checkpoint(700, 150),
            Checkpoint(700, 450),
            Checkpoint(400, 500),
            Checkpoint(100, 450),
            Checkpoint(100, 150),
            Checkpoint(400, 100)
        ]
        self.current_checkpoint = 0
        self.lap = 1
        self.start_time = pygame.time.get_ticks()
        self.game_finished = False
        self.final_time = 0
    
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_r and self.game_finished:
                        self.reset_game()
            
            # Get pressed keys
            keys = pygame.key.get_pressed()
            
            # Update game
            if not self.game_finished:
                self.car.update(keys)
                self.update_checkpoints()
            
            # Draw everything
            self.draw_track()
            
            # Draw checkpoints
            for checkpoint in self.checkpoints:
                checkpoint.draw(self.screen)
            
            # Highlight current checkpoint
            current_cp = self.checkpoints[self.current_checkpoint]
            pygame.draw.rect(self.screen, YELLOW, current_cp.rect, 4)
            
            self.car.draw(self.screen)
            self.draw_ui()
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = RacingGame()
    game.run()