import pygame
import sqlite3
from pygame.locals import *
from config import *
from objects.asteroid import Asteroid
from objects.ship import Ship

# Initialize Pygame
pygame.init()

# Set up some properties
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)


def game_loop(cursor):
    # Sprite groups
    all_sprites = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Create the player
    player = Ship()
    all_sprites.add(player)

    # Create the asteroids
    for i in range(10):
        asteroid = Asteroid()
        all_sprites.add(asteroid)
        asteroids.add(asteroid)

    # Score
    score = 0

    # Load the high score
    cursor.execute("SELECT MAX(score) FROM scores")
    high_score = cursor.fetchone()[0]
    if high_score is None:
        high_score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Update
        all_sprites.update()

        # Collision detection
        hits = pygame.sprite.spritecollide(player, asteroids, False)
        if hits:
            # Game over
            return score

        # Draw everything
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        # Draw the score
        score_text = font.render(str(score), True, WHITE)
        screen.blit(score_text, (10, 10))

        # Draw the high score
        high_score_text = font.render(str(high_score), True, WHITE)
        screen.blit(high_score_text, (SCREEN_WIDTH - 100, 10))

        pygame.display.flip()
        clock.tick(60)

        # Increase the score
        score += 1

def main():
    # Connect to the SQLite database
    conn = sqlite3.connect(DATABASE)

    # Create the database if it doesn't exist
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS scores (score INTEGER)")

    # Run the game loop
    score = game_loop(cursor)

    # Save the score
    cursor.execute("INSERT INTO scores (score) VALUES (?)", (score,))
    conn.commit()

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
