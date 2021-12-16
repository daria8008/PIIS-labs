import pygame
import time
from itertools import count
from training import *
from input_extraction import *
import result_csv
import images
from pacman import Pacman
from ghost import Ghost
from common import Position
import app_config
import display
import map
import state_file
import matplotlib.pyplot as plt


def check_game_end():
    for i in range(len(map.coins_map.map)):
        for j in range(len(map.coins_map.map[i])):
            if map.coins_map.map[i][j] == 1:
                return False
    return True


def check_pacman_die():
    for ghost in ghosts:
        if ghost.x == pacman.x and ghost.y == pacman.y:
            return True
    return False


result_csv = result_csv.StatisticsDQN()

pygame.init()
clock = pygame.time.Clock()

images.load_images()
display.init()

run = True
pacman = Pacman(app_config.PLAYER_START_POS_X, app_config.PLAYER_START_POS_Y)

ghosts = []
for i in range(app_config.enemies_cnt):
    (posX, posY) = app_config.ghosts_start_positions[i]
    ghosts.append(Ghost(i, posX, posY, 0, 0))


plt.figure()
plt.imshow(get_screen().cpu().squeeze(0).permute(1, 2, 0).numpy(), interpolation='none')
plt.title('Example extracted screen')
plt.plot()

num_episodes = 300
for i_episode in range(num_episodes):
    print("game ", i_episode, ", Score: ", state_file.score)
    start_time = time.time()

    state_file.score = 0
    display.init()

    pacman = Pacman(app_config.PLAYER_START_POS_X, app_config.PLAYER_START_POS_Y)

    ghosts = []
    for i in range(app_config.enemies_cnt):
        (posX, posY) = app_config.ghosts_start_positions[i]
        ghosts.append(Ghost(i, posX, posY, 0, 0))

    last_screen = get_screen()
    current_screen = get_screen()
    state = current_screen - last_screen

    for t in count():
        previous_score = state_file.score
        temp_state = state
        action = select_action(state)

        display.display_score()

        if not check_game_end() and not check_pacman_die():
            next_state = current_screen - last_screen
        else:
            next_state = None

        pacman.walk(action.item())
        pacman.eat_coins()



        for ghost in ghosts:
            ghost.walk_optimal(Position(pacman.x, pacman.y))
            #ghost.walk_random(Position(pacman.x, pacman.y))

        display.draw_window()
        display.display_score()
        display.draw_agent(pacman)
        map.spawn_coins()

        for ghost in ghosts:
            display.draw_agent(ghost)
        display.update_screen()

        reward = state_file.score - previous_score
        reward = torch.tensor([reward], device=device)

        last_screen = current_screen
        current_screen = get_screen()



        memory.push(state, action, next_state, reward)
        state = next_state

        optimize_model()

        if check_game_end() or check_pacman_die():
            episode_durations.append(t + 1)
            scores.append(state_file.score)
            map.coins_map.update()
            break

    result_csv.add_statistics(i_episode, state_file.score, time.time() - start_time)

    if i_episode % TARGET_UPDATE == 0:
        target_net.load_state_dict(policy_net.state_dict())

print('Complete')
plt.ioff()
plt.clf()
plot_score()
