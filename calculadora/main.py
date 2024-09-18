import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}', '{tb5.value}'."
        page.update()
        
    t = ft.Text()
    tb1 = ft.TextField(label="+")
    tb2 = ft.TextField(label="Disabled", disabled=True, value="-")
    tb3 = ft.TextField(label="Read-only", read_only=True, value="x")
    tb4 = ft.TextField(label="With placeholder", hint_text="/")
    tb5 = ft.TextField(label="With an icon", icon=ft.icons"borrar")
    b = ft.ElevatedButton(text="borrar", on_click=(borrar))
    page.add(tb1, tb2, tb3, tb4, tb5, b, t)

ft.app(main)
