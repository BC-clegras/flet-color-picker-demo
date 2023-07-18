import flet as ft
from color_picker import ColorPicker
from math import pi


class Demo(ft.Stack):
    def __init__(self, page):
        super().__init__()
        self.controls = []
        self.page = page

    def did_mount(self):
        self.gradient_demo = GradientDemo(page=self.page)

        self.controls.append(self.gradient_demo)

        self.color_picker = ft.Container(
            content=ColorPicker(page=self.page),
            padding=ft.padding.symmetric(vertical=10, horizontal=10),
            bgcolor=ft.colors.WHITE,
            border_radius=5,
            width=250,
            height=500,
            top=0,
            left=0,
        )

        self.controls.append(self.color_picker)

        self.update()


class GradientDemo(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.alignment = ft.alignment.center

        self.gradient = ft.LinearGradient(
            begin=ft.alignment.top_right,
            end=ft.Alignment(1, 1),
            colors=[],
            rotation=pi / 4,
        )
        self.width = 150
        self.height = 150
        self.border_radius = 5
        self.border = ft.border.all(1)
        self.top = 0
        self.left = 300

        self.page = page
