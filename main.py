import flet as ft
import logging
from Music.Comp import Track

tracks = []
logging.basicConfig(filename='app.log', level=logging.INFO)

def create_input_form():
    logging.info("Input form created")
    name_field = ft.TextField(label="Название песни", width=300)
    author_field = ft.TextField(label="Имя автора", width=300)
    creation_date_field = ft.TextField(label="Дата создания", width=300)
    play_time_field = ft.TextField(label="Длительность песни", width=300)
    text_field = ft.TextField(label="Текст песни", width=300, multiline=True)

    def save_button_click(e):
        if not (name_field.value == ""):
            if not (author_field.value == ""):
                if not (creation_date_field.value == ""):
                    if not (play_time_field.value == ""):
                        if not (text_field.value == ""):
                            track = Track(name_field.value, author_field.value, creation_date_field.value, play_time_field.value, text_field.value)
                            tracks.append(track)
                            logging.info("data saved")
                            name_field.value = ""
                            author_field.value = ""
                            creation_date_field.value = ""
                            play_time_field.value = ""
                            text_field.value = ""

    save_button = ft.ElevatedButton("Save", on_click=save_button_click)

    return ft.Column(
        [
            name_field,
            author_field,
            creation_date_field,
            play_time_field,
            text_field,
            save_button,
            ft.Text("")
        ]
    )


def create_data_table():
    columns = [
        ft.DataColumn(ft.Text("Name Track")),
        ft.DataColumn(ft.Text("Authors name")),
        ft.DataColumn(ft.Text("Creation date")),
        ft.DataColumn(ft.Text("Play time")),
        ft.DataColumn(ft.Text("Text"))
    ]

    def create_data_row(track):
        return ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(track.name)),
                ft.DataCell(ft.Text(track.author)),
                ft.DataCell(ft.Text(track.creation_date)),
                ft.DataCell(ft.Text(track.play_time)),
                ft.DataCell(ft.Text(track.text))
            ]
        )

    data_table = ft.DataTable(columns=columns, rows=[create_data_row(track) for track in tracks])
    logging.info("Table created")
    return data_table



def main(page: ft.Page):
    logging.info("Program started")

    data_table = create_data_table()

    input_form = create_input_form()

    def update_table(e):
        data_table.rows = [create_data_row(track) for track in tracks]
        page.update()
        logging.info("Table updated")



    def create_data_row(track):
        logging.info("Table created")
        return ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(track.name)),
                ft.DataCell(ft.Text(track.author)),
                ft.DataCell(ft.Text(track.creation_date)),
                ft.DataCell(ft.Text(track.play_time)),
                ft.DataCell(ft.Text(track.text))
            ]
        )

    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Список песен",
                content=ft.Container(
                    content=data_table, alignment=ft.alignment.top_center
                ),
            ),
            ft.Tab(
                text="Добавить песню",
                icon=ft.icons.ADD,
                content=ft.Container(
                    content=input_form, alignment=ft.alignment.top_center
                ),
            ),
        ],
        expand=1,
    )


    page.title = "Приложение для изучения музыки"
    page.horizontal_alignment = "center"
    page.add(t)
    page.add(ft.ElevatedButton("Обновить список", on_click=lambda e: update_table(e)))

if __name__ == '__main__':
    ft.app(main)