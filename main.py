import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from powerup import PowerUp


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))




def main():
    print("Starting Asteroids!")
    print("Level 1")

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    PowerUp.containers = (powerups, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    

    dt = 0
    fps = 0
    score = 0
    total_time = 0
    shield_cooldown = 0
    shield_text = FONT.render("Shield Active", True, 'cyan')
    invincible_text_width = FONT.size(f"INVINCIBLE FOR 0 SECONDS")[0]
    nuke_text = BIGFONT.render("NUCLEAR DETONATION", True, "Red")
    nuke_text_width = BIGFONT.size("NUCLEAR DETONATION")[0]
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Timetracking
        total_time += dt
        int_time = int(total_time)
        shield_cooldown -= dt
        if dt != 0:
            fps = int(1/dt)
        # print(fps)

        # Update Objects
        for item in updatable:
            item.update(dt)
        
        for ast in asteroids:
            if ast.check_collision(player):
                if player.invincible == False and shield_cooldown <= 0:
                    player.lives -= 1
                    shield_cooldown = POWERUP_SHIELD_COOLDOWN
                    if player.lives == 1:
                        player.shielded = False
                    if player.lives == 0:
                        print("Game over!")
                        print("Score:", score)
                        print("Time:",int_time)
                        # return
                    else:
                        ast.split()

            for shot in shots:
                if ast.check_collision(shot):
                    ast.split()
                    if not player.piercing_shot:
                        shot.kill()
                    score += 1
        for pow in powerups:
            if pow.check_collision(player):
                player.apply_powerup(pow)
                score += 10
                if pow.type == "nuke":
                    score += 90
                    for ast in asteroids:
                        ast.split()
                pow.kill()

        # Update Text
        score_text = FONT.render(f"Score: {score}", True, 'white')
        time_text = FONT.render(f"Time: {int_time}", True, 'white')

        if player.invincible: invincible_text = FONT.render(f"INVINCIBLE FOR {int(POWERUP_INVINCIBILITY_TIME - player.time_invincible)} SECONDS", True, 'green')
        
        if player.fast_fire: fast_fire_text = FONT.render(f"Fast Shots: {int(POWERUP_FAST_FIRE_TIME - player.time_fast_fire)}", True, 'yellow')
        if player.piercing_shot: piercing_text = FONT.render(f"Piercing Shots: {int(POWERUP_PIERCING_SHOT_TIME - player.time_piercing_shot)}", True, 'yellow')
        if player.backward_shot: backward_text = FONT.render(f"Backward Shots: {int(POWERUP_BACKWARD_SHOT_TIME - player.time_backward_shot)}", True, 'yellow')
        if player.triple_shot: triple_text = FONT.render(f"Triple Shots: {int(POWERUP_TRIPLE_SHOT_TIME - player.time_triple_shot)}", True, 'White')

        

        # Render
        screen.fill((0,0,0))
        for item in drawable:
            item.draw(screen)
        
        # On-Screen Text
        screen.blit(score_text, (5, 5))
        screen.blit(time_text, (150, 5))
        if player.shielded: screen.blit(shield_text, (5, SCREEN_HEIGHT - 25))
        if player.invincible: screen.blit(invincible_text, ((SCREEN_WIDTH - invincible_text_width)//2, SCREEN_HEIGHT - 25))
        if player.fast_fire: screen.blit(fast_fire_text, (5, SCREEN_HEIGHT - 50))
        if player.piercing_shot: screen.blit(piercing_text, (5, SCREEN_HEIGHT - 75))
        if player.backward_shot: screen.blit(backward_text, (5, SCREEN_HEIGHT - 100))
        if player.triple_shot: screen.blit(triple_text, (5, SCREEN_HEIGHT - 125))
        if player.just_nuked and int(player.time_just_nuked*10+1) % 2 == 0: screen.blit(nuke_text,((SCREEN_WIDTH - nuke_text_width)//2, 20))

        # Display flip
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
