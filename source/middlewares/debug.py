class libDebug():
    def __init__(self) -> None:
        self.BOLD = "\033[1m"
        self.RED = "\033[31m"
        self.GREEN = "\033[32m"
        self.RESET = "\033[0m"
        self.ORANGE = "\033[33m"
        
    def printError(self, error) -> None:
        return print(f"{self.BOLD}{self.RED}ERROR: {self.RESET}{error}")
    
    def printWarning(self, error) -> None:
        return print(f"{self.BOLD}{self.ORANGE}WARNING: {self.RESET}{error}")

    def printSuccess(self, success) -> None:
        return print(f"{self.BOLD}{self.GREEN}SUCCESS: {self.RESET}{success}")

    def printTitle(self, title) -> None:
        menubar = "—" * len(title)
        return print(f"{self.BOLD}{menubar} {title} {menubar} {self.RESET}")