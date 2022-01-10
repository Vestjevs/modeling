import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np

import modeling as mod

elements = [mod.Element(1.5, 1.7, 1.2, 0.5),
            mod.Element(1.1, 1.5, 0.7, 0.4),
            mod.Element(1.1, 1.2, 0.6, 0.9),
            mod.Element(2.1, 2.3, 0.2, 1.1)]

r_i = [i for i in range(3, 23)]
t_i = [i for i in range(2, 22)]

p_0 = 1.2


def p():
    p = []
    for r, t in zip(r_i, t_i):
        for elem in elements:
            elem.generate_q()
        p.append(mod.P(r, t, p_0, elements, [i for i in range(1, t)]))
    return p


app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Моделирование", ),
        html.P(
            children="Моделирование задачи",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": t_i,
                        "y": p(),
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
                   host='127.0.0.1')
