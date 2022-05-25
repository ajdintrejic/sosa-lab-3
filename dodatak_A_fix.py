import getpass
import bcrypt

class OperationsManager:
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def perform_division(self) -> float:
        try:
            self.a = float(self.a)
            self.b = float(self.b)
            if self.b != 0.:
                raise Exception('a')
        except:
            return float('nan')

        """Divides a with b. If b is zero, returns NaN."""
        return self.a / self.b


if __name__ == "__main__":
    user = input("Username: ")
    password = str.encode(getpass.getpass("Password: "))
    hashed = b'$2b$12$a7NMd/tw/gjVRVmNw435WuS39swRtsILU1eYHPpJHU/z7H54HyPty'

    if bcrypt.checkpw(password, hashed):
        p = True
    else:
        p = False

    if user != "root" or not p:
        print("Wrong username or password!")
        exit(0)
    else:
        print("Login success!")
        a = float(input("A = "))
        b = float(input("B = "))
        ops_manager = OperationsManager(a, b)
        print(ops_manager.perform_division())
