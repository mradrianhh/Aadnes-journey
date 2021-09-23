class Character():
    __name: str

    # Getters and setters.

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name