class Player():
    __username: str

    # Getters and setters.

    def get_username(self) -> str:
        return self.__username

    def set_username(self, username: str) -> None:
        self.__username = username