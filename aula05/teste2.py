import curses

def exibir_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "===== MENU =====")
    stdscr.addstr(2, 0, "1. Opção 1")
    stdscr.addstr(3, 0, "2. Opção 2")
    stdscr.addstr(4, 0, "3. Opção 3")
    stdscr.addstr(5, 0, "0. Sair")

def main():
    curses.wrapper(exibir_menu)

if __name__ == "__main__":
    main()
