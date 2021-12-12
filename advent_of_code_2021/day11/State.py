import dataclasses


@dataclasses.dataclass
class State:
    value: int
    flash: bool

    def reset(self):
        if self.flash:
            self.value = 0
            self.flash = False
