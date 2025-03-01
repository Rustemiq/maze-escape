import pygame

from modules.constants import *


def mapping(x, y):
    return int((x // TILE_SIZE) * TILE_SIZE), int((y // TILE_SIZE) * TILE_SIZE)


def is_wall(x, y, maze):
    try:
        return maze[int(y // TILE_SIZE)][int(x // TILE_SIZE)]
    except IndexError:
        return True


def ray_casting(screen, player_pos, player_direction, maze):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_direction = player_direction - FOV / 2
    is_finish = False
    for ray in range(NUM_RAYS):
        depth_h, depth_v = None, None
        v_wall, h_wall = (0, 0), (0, 0)
        sin_d = math.sin(cur_direction)
        cos_d = math.cos(cur_direction)
        x, dx = (xm + TILE_SIZE, 1) if cos_d >= 0 else (xm, -1)
        for i in range(0, WIDTH, int(TILE_SIZE)):
            if cos_d != 0:
                depth_v = (x - ox) / cos_d
                y = oy + depth_v * sin_d
                v_wall = int(x // TILE_SIZE), int(y // TILE_SIZE)
                if is_wall(*mapping(x + dx, y), maze):
                    break
                x += dx * TILE_SIZE
        y, dy = (ym + TILE_SIZE, 1) if sin_d >= 0 else (ym, -1)
        for i in range(0, HEIGHT, int(TILE_SIZE)):
            if sin_d != 0:
                depth_h = (y - oy) / sin_d
                x = ox + depth_h * cos_d
                h_wall = int(x // TILE_SIZE), int(y // TILE_SIZE)
                if is_wall(*mapping(x, y + dy), maze):
                    break
                y += dy * TILE_SIZE
        if depth_v is None:
            wall = h_wall
            depth = depth_h
        if depth_h is None:
            wall = v_wall
            depth = depth_v
        else:
            if depth_h < depth_v:
                depth = depth_h
                wall = h_wall
            else:
                depth = depth_v
                wall = v_wall

        depth *= math.cos(player_direction - cur_direction)
        if depth != 0:
            proj_height = PROJ_COEFF / depth
        else:
            proj_height = 0
        c = 255 / (1 + depth ** 2 / 10000)
        if wall == FINISH:
            color = c, c / 2, c / 2
            is_finish = True
        else:
            color = c / 2, c, c / 2
        pygame.draw.rect(
            screen,
            color,
            (
                ray * PROJ_SCALE,
                HEIGHT // 2 - proj_height // 2,
                PROJ_SCALE,
                proj_height,
            ),
        )
        cur_direction += DELTA_ANGLE
    return is_finish