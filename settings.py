class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_speed = 1.5
        self.ship_up_speed = 1

        #bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 191, 255)
        self.bullets_allowed = 3