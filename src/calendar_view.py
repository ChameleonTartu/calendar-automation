from rich.text import Text

from textual.app import App, ComposeResult
from textual.widgets import DataTable

ROWS = [
    ('Mon', 'Tue', 'Wed', 'Th', 'Fri', 'Sat', 'Sun'),
    (1, 2, 3),
    (4, 5, 6, 7, 8, 9, 10)
]

LIGHT_YELLOW = '#fce8b2'
LIGHT_GREEN = '#b7e1cd'


class TableApp(App):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])

        first_line_of_the_month = ["" for _ in range(max(0, len(ROWS[0]) - len(ROWS[1])))] + list(ROWS[1])
        table.add_row(*[Text(str(cell), style='#fce8b2', justify="right") for cell in first_line_of_the_month])

        # TODO: Understand how to apply backgroun colors.
        a = Text(str(1), justify="right")
        a.style.background_style = LIGHT_YELLOW
        table.add_row(dir(a))

        for row in ROWS[2:]:
            styled_row = [
                Text(str(cell), justify="right") for cell in row
            ]
            table.add_row(*styled_row)


app = TableApp()
if __name__ == "__main__":
    app.run()
