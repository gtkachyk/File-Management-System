from instance import Instance
from controller import Controller

def main ():
    A = Instance("A", 10)
    B = Controller("B", 5, [])
    B.add_instance(A)
    B.print_network()

main()