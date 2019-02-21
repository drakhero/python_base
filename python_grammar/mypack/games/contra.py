def play():
    print("正在玩魂斗罗......")

def gameover():
    '''
    此函数会在游戏结束时调用
    然后此函数调用菜单　mypack.menu里的show_menu
    '''
    print("game over!")

    from ..menu import show_menu
    show_menu()


print("魂斗罗　模块被加载")

