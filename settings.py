class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_speed = 1.5
        self.ship_up_speed = 1
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (0, 191, 255)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 30
        # fleet_direction of 1 represenets right; -1 represents left.
        self.fleet_direction = 1
