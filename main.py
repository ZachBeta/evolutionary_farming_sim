#!/usr/bin/env python3
"""
Main entry point for the Evolutionary Farming Simulator.
"""
import sys
import pygame
from pathlib import Path
from typing import Tuple, List

# Add project root to Python path
sys.path.append(str(Path(__file__).parent.parent))

# Constants
TILE_SIZE = 64  # Size of each grid cell in pixels
GRID_WIDTH, GRID_HEIGHT = 40, 30  # Grid size in tiles
SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 768  # Window size
FPS = 60

# Colors
GRASS_GREEN = (34, 139, 34)
SOIL_BROWN = (139, 69, 19)
GRID_LINE = (50, 50, 50)

class World:
    """Represents the game world with a grid-based map."""
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.camera_x = 0
        self.camera_y = 0
        
        # Create a simple heightmap (0 = water, 1 = sand, 2 = grass, 3 = dirt)
        self.tiles = [[self._generate_tile(x, y) for x in range(width)] for y in range(height)]
    
    def _generate_tile(self, x: int, y: int) -> int:
        """Generate a tile type based on position (simple noise-like pattern)."""
        import math
        value = math.sin(x * 0.1) * math.cos(y * 0.1) * 2
        return max(0, min(3, int(value + 2)))
    
    def get_tile_color(self, tile_type: int) -> Tuple[int, int, int]:
        """Get the color for a tile type."""
        colors = [
            (65, 105, 225),  # Water (blue)
            (238, 214, 175),  # Sand (beige)
            (34, 139, 34),    # Grass (green)
            (139, 69, 19)     # Dirt (brown)
        ]
        return colors[tile_type] if 0 <= tile_type < len(colors) else (0, 0, 0)
    
    def draw(self, screen: pygame.Surface, camera_x: int, camera_y: int):
        """Draw the world grid."""
        screen_width, screen_height = screen.get_size()
        
        # Calculate visible tiles
        start_x = max(0, camera_x // TILE_SIZE)
        start_y = max(0, camera_y // TILE_SIZE)
        end_x = min(self.width, (camera_x + screen_width) // TILE_SIZE + 1)
        end_y = min(self.height, (camera_y + screen_height) // TILE_SIZE + 1)
        
        # Draw tiles
        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                tile_x = x * TILE_SIZE - camera_x
                tile_y = y * TILE_SIZE - camera_y
                
                # Draw tile background
                tile_type = self.tiles[y][x]
                pygame.draw.rect(
                    screen,
                    self.get_tile_color(tile_type),
                    (tile_x, tile_y, TILE_SIZE, TILE_SIZE)
                )
                
                # Draw grid lines
                pygame.draw.rect(
                    screen,
                    GRID_LINE,
                    (tile_x, tile_y, TILE_SIZE, TILE_SIZE),
                    1  # Line width
                )

def main():
    """Initialize and run the main game loop."""
    print("Starting Evolutionary Farming Simulator...")
    
    # Initialize Pygame
    pygame.init()
    
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Evolutionary Farming Simulator")
    
    # Create the game world
    world = World(GRID_WIDTH, GRID_HEIGHT)
    
    # Camera position
    camera_x, camera_y = 0, 0
    camera_speed = 500  # pixels per second
    
    # Main game loop
    running = True
    clock = pygame.time.Clock()
    dt = 0  # Delta time in seconds
    
    try:
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.VIDEORESIZE:
                    # Handle window resizing
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            
            # Handle camera movement with arrow keys
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                camera_x = max(0, camera_x - int(camera_speed * dt))
            if keys[pygame.K_RIGHT]:
                camera_x = min(world.width * TILE_SIZE - screen.get_width(), 
                             camera_x + int(camera_speed * dt))
            if keys[pygame.K_UP]:
                camera_y = max(0, camera_y - int(camera_speed * dt))
            if keys[pygame.K_DOWN]:
                camera_y = min(world.height * TILE_SIZE - screen.get_height(), 
                             camera_y + int(camera_speed * dt))
            
            # Clear the screen
            screen.fill(GRASS_GREEN)
            
            # Draw the world
            world.draw(screen, camera_x, camera_y)
            
            # Draw debug info
            font = pygame.font.Font(None, 24)
            debug_text = f"Camera: ({camera_x}, {camera_y}) | FPS: {int(clock.get_fps())}"
            debug_surface = font.render(debug_text, True, (255, 255, 255))
            screen.blit(debug_surface, (10, 10))
            
            # Update the display
            pygame.display.flip()
            
            # Cap the frame rate and get delta time
            dt = clock.tick(FPS) / 1000.0
            
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        pygame.quit()
        sys.exit()
        sys.exit()

if __name__ == "__main__":
    main()
