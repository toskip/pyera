from base.skill import Skill


class Skill0000(Skill):
    def __init__(self):
        super().__init__()
        self.name = '全副武装'
        self.mp_cost = 2
    def on_use(self):
        pass
