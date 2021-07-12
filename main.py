import pygame
import board


def main():
    b = board.Board()
    while b.winner is None:
        print(b)
        col = int(input("Enter a column : "))
        b.move(col)
    print(b)
    print(f"winner is : {b.winner}")


if __name__ == '__main__':
    main()
