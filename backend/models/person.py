class Person:
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def greet(self) -> str:
        return f"Hello, my name is {self.name}."
