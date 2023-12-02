import math

# config.py

# Frame per second limit
FPS_LIMIT = 60

# Animation
ANIMATION_SPEED = 10
SLEEP_TIME = 0.2
CAPTURE_PHASES = [1, 2]

# House gap
HOUSE_GAP = 60

# Game colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 102)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SELECTION_THICKNESS = 10

# Player details
PLAYER_1 = 1
PLAYER_2 = 2
PLAYER_NUMBERS = [PLAYER_1, PLAYER_2]

# Game board
INIT_SEEDS = 7 # 3 | 6 | 7
INIT_HOUSE_ROW = INIT_SEEDS # 6 | 7
TOTAL_HOUSE = INIT_HOUSE_ROW * 2 # 12 | 14
MAX_HOUSE_COUNT = (INIT_SEEDS + 1) * 2 # 14 | 16
MAX_INDEX = MAX_HOUSE_COUNT - 1 # 13 | 15
BOARD_HOUSES = [INIT_SEEDS] * INIT_HOUSE_ROW + [0] + [INIT_SEEDS] * INIT_HOUSE_ROW + [0]

# Pygame Screen Dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
GAP_RATIO = 0.3
GAP = SCREEN_WIDTH * GAP_RATIO // (INIT_HOUSE_ROW + 1) 
TOP_ROW_Y = 0.4 * SCREEN_HEIGHT
BOTTOM_ROW_Y = TOP_ROW_Y + 2 * GAP
CENTER_ROW = TOP_ROW_Y + GAP

HOUSE_CENTER = 20 # SCREEN_HEIGHT // 16


# Game houses
PLAYER_1_STORE = MAX_INDEX # 7 | 13 | 15
PLAYER_2_STORE = INIT_HOUSE_ROW # 3 | 6 | 7
PLAYER_1_MIN_HOUSE = PLAYER_2_STORE + 1 # 7 | 8
PLAYER_1_MAX_HOUSE = PLAYER_1_STORE - 1 # 12 | 14
PLAYER_2_MIN_HOUSE = 0 # 0 | 0
PLAYER_2_MAX_HOUSE = PLAYER_2_STORE - 1 # 5 | 6
STORE_INDICES = [PLAYER_1_STORE, PLAYER_2_STORE]

# Seed font and size
SEED_FONT = None
SEED_FONT_SIZE = 50
SEED_COLOR = WHITE
STORE_SEED_FONT = None
STORE_SEED_FONT_SIZE = 60
HOUSE_INDEX_FONT = None
HOUSE_INDEX_FONT_SIZE = 15
HOUSE_INDEX_COLOR = YELLOW

# cursor
CURSOR_IMAGE = "../assets/handcursor.png"
CURSOR_FONT = None
CURSOR_FONT_SIZE = 36
CURSOR_FONT_COLOR = BLACK

# pause message font and size
PAUSE_FONT = None
PAUSE_FONT_SIZE = 36
PAUSE_MSG_COLOR = RED
PAUSE_MSG_DIM = (0.4 * SCREEN_WIDTH, 0.47 * SCREEN_HEIGHT)

# capture message font and size
CAPTURE_FONT = None
CAPTURE_FONT_SIZE = 36
CAPTURE_MSG_COLOR = RED
CAPTURE_MSG_DIM = (0.4 * SCREEN_WIDTH, 0.47 * SCREEN_HEIGHT)

# pause button 
PAUSE_BUTTON_FONT = None
PAUSE_BUTTON_FONT_SIZE = 36
PAUSE_BUTTON_DIM = (10, 70, 100, 50)
PAUSE_BUTTON_COLOR = BLACK

# Restart button
RESTART_BUTTON_FONT = None
RESTART_BUTTON_FONT_SIZE = 36
RESTART_BUTTON_DIM = (10, 10, 100, 50)
RESTART_BUTTON_COLOR = BLACK

# House sizes
STORE_SIZE = SCREEN_HEIGHT // 10
HOUSE_SIZE = SCREEN_HEIGHT // 16

# Colors and messages
SCREEN_FILL_COLOR = WHITE

# turn message font and size
TURN_MSG_FONT = None
TURN_MSG_FONT_SIZE = 36
TURN_MSG_COLOR = BLACK
