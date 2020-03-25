from os import path


def image_path(image):
    return f"{path.dirname(__file__)}/images/{image}"


player_image = image_path("player.png")
spike_image = image_path("spike.png")
spike_under_image = image_path("spike_under.png")
coin_image = image_path("coin.png")


level1 = [
    {
        "type": "player",
        "sprite_type": "image",
        "image": player_image,
        "coords": (390, 380),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (0, 400),
        "dimensions": (800, 200),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (600, 380),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (780, 380),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (900, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (1200, 580),
        "dimensions": (100, 20),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "reward",
        "sprite_type": "image",
        "image": coin_image,
        "coords": (1220, 555),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (1300, 560),
        "dimensions": (100, 40),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "reward",
        "sprite_type": "image",
        "image": coin_image,
        "coords": (1320, 535),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (1400, 540),
        "dimensions": (100, 60),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "reward",
        "sprite_type": "image",
        "image": coin_image,
        "coords": (1420, 515),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (1500, 560),
        "dimensions": (100, 40),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "reward",
        "sprite_type": "image",
        "image": coin_image,
        "coords": (1520, 535),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (1600, 580),
        "dimensions": (100, 20),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (2000, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (2150, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (2300, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (2450, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (2600, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (2750, 530),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_under_image,
        "coords": (2750, 550),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (2900, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "goal",
        "sprite_type": "rectangle",
        "coords": (3100, 0),
        "dimensions": (800, 600),
        "fill": "white",
        "outline": "white",
    },
]

level2 = [
    {
        "type": "player",
        "sprite_type": "image",
        "image": player_image,
        "coords": (390, 380),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (0, 400),
        "dimensions": (800, 200),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (805, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (825, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (845, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (865, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (885, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (905, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (925, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (950, 400),
        "dimensions": (50, 200),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (1000, 350),
        "dimensions": (20, 250),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (1020, 300),
        "dimensions": (20, 300),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (1200, 540),
        "dimensions": (620, 20),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (1800, 550),
        "dimensions": (20, 50),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (1200, 480),
        "dimensions": (620, 20),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1640, 460),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1700, 460),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1760, 460),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (1200, 420),
        "dimensions": (620, 20),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1400, 400),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1500, 400),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1600, 400),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1700, 400),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1800, 400),
        "dimensions": (20, 20),
    },
    {
        "type": "reward",
        "sprite_type": "image",
        "image": coin_image,
        "coords": (1950, 520),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (2120, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "reward",
        "sprite_type": "image",
        "image": coin_image,
        "coords": (2120, 520),
        "dimensions": (20, 20),
    },
    {
        "type": "goal",
        "sprite_type": "rectangle",
        "coords": (2300, 0),
        "dimensions": (800, 600),
        "fill": "white",
        "outline": "white",
    },
]


level3 = [
    {
        "type": "player",
        "sprite_type": "image",
        "image": player_image,
        "coords": (390, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (580, 580),
        "dimensions": (100, 20),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (680, 560),
        "dimensions": (100, 40),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (780, 540),
        "dimensions": (100, 60),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (880, 520),
        "dimensions": (100, 80),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (980, 500),
        "dimensions": (100, 100),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (1080, 480),
        "dimensions": (100, 120),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1200, 480),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_under_image,
        "coords": (1200, 500),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1220, 480),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_under_image,
        "coords": (1220, 500),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (1260, 460),
        "dimensions": (100, 140),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1360, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1380, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1400, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1420, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (1440, 440),
        "dimensions": (100, 160),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1540, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1560, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1580, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1600, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (1620, 420),
        "dimensions": (300, 180),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (2000, 420),
        "dimensions": (100, 30),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "reward",
        "sprite_type": "image",
        "image": coin_image,
        "coords": (2040, 390),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (2100, 400),
        "dimensions": (100, 50),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (2200, 380),
        "dimensions": (100, 70),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (2300, 360),
        "dimensions": (100, 90),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "reward",
        "sprite_type": "image",
        "image": coin_image,
        "coords": (2340, 330),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (2400, 340),
        "dimensions": (100, 110),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (2500, 320),
        "dimensions": (100, 130),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (2600, 300),
        "dimensions": (100, 150),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "reward",
        "sprite_type": "image",
        "image": coin_image,
        "coords": (2640, 270),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (2700, 280),
        "dimensions": (100, 170),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (2800, 260),
        "dimensions": (100, 190),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (2900, 240),
        "dimensions": (100, 210),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "reward",
        "sprite_type": "image",
        "image": coin_image,
        "coords": (2940, 210),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (3000, 220),
        "dimensions": (100, 230),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (3100, 200),
        "dimensions": (100, 250),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (3200, 180),
        "dimensions": (100, 270),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "reward",
        "sprite_type": "image",
        "image": coin_image,
        "coords": (3240, 150),
        "dimensions": (20, 20),
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (3300, 160),
        "dimensions": (100, 290),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "surface",
        "sprite_type": "rectangle",
        "coords": (3400, 140),
        "dimensions": (100, 310),
        "fill": "black",
        "outline": "black",
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1920, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1940, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1960, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "obstacle",
        "sprite_type": "image",
        "image": spike_image,
        "coords": (1980, 580),
        "dimensions": (20, 20),
    },
    {
        "type": "goal",
        "sprite_type": "rectangle",
        "coords": (2100, 450),
        "dimensions": (800, 150),
        "fill": "white",
        "outline": "white",
    },
    {
        "type": "goal",
        "sprite_type": "rectangle",
        "coords": (3500, 0),
        "dimensions": (800, 600),
        "fill": "white",
        "outline": "white",
    },
]


LEVELS = [{"Level 1": level1, "Level 2": level2, "Level 3": level3}]
