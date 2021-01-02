from modules.color import Color


class Ball:
    def __init__(self, color: Color):
        self.color = color

    def __eq__(self, other: 'Ball'):  # type: ignore
        return self.color is other.color

    def __repr__(self):
        return f'Ball({self.color.verbose_name})'

    def __str__(self) -> str:
        return str(self.color)
