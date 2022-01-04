import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np

import modeling as mod

t = np.arange(1, 2, .01)
p_r_t = np.array([mod.p(x) for x in t])

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Моделирование",),
        html.P(
            children="Моделирование задачи",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": t,
                        "y": p_r_t,
                        "type": "lines",
                    },
                ],
                "layout": {"title": "График давления"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True,
                   host = '127.0.0.1')