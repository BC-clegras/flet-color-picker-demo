import flet as ft
from demo import Demo


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.demo_stack = Demo(page=page)

    page.bgcolor = ft.colors.WHITE

    page.add(page.demo_stack)

    page.update()


ft.app(target=main)
