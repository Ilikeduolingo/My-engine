class EntityData:
    def __init__(self, name: str, x: float, y: float):
        self.name = name
        self.x = x
        self.y = y

    def serialize(self) -> str:
        """Convert entity data to a string for sending."""
        return f"{self.name},{self.x},{self.y}"

    @staticmethod
    def deserialize(data: str):
        """Convert received string back into an EntityData object."""
        try:
            name, x, y = data.split(',')
            return EntityData(name, float(x), float(y))
        except ValueError:
            return None  # Handle malformed data
