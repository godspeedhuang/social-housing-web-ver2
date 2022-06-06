from dash import html,dcc
import dash_bootstrap_components as dbc

def tab_higher_adhesion(
    score_weighted:list,
)->html.Div:
    """
    Return a HTML div of user set score wighted for higher adhesion public

    :param score_weighted: list, default score weighted [周邊社區開放資料, 周邊社區民眾參與, 社宅民眾參與 ]
    """
    return html.Div([
        # 周邊社區居民
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        dbc.Row([
                            dbc.Col([
                                html.Div([
                                    html.Label('周邊社區居民',className='text-secondary'),
                                    html.H6('開放資料分析 權重'),
                                    dcc.Input(
                                        id='surrounding-opendata-weighted',
                                        value=score_weighted[0],
                                        type='number',
                                        min=0.0,
                                        max=1.0,
                                        step=0.01,
                                        debounce=True
                                    )
                                ],className='border border-secondary rounded p-2 m-1')
                            ],width=6),
                            dbc.Col([
                                html.Div([
                                    html.Label('周邊社區居民',className='text-secondary'),
                                    html.H6('民眾參與分析 權重'),
                                    dcc.Input(
                                        id='surrounding-people-weighted',
                                        value=score_weighted[1],
                                        type='number',
                                        min=0.0,
                                        max=1.0,
                                        step=0.01,
                                        debounce=True
                                    )  
                                ],className='border border-secondary rounded p-2 my-1 ')
                            ],width=6),
                        ]),
                    ],width=8),
                    dbc.Col([
                        html.Div([
                            html.Label('社宅居民',className='text-secondary'),
                            html.H6('民眾參與分析 權重'),
                            dcc.Input(
                                id='social-housing-people-weighted',
                                value=score_weighted[2],
                                type='number',
                                min=0.0,
                                max=1.0,
                                step=0.01,
                                debounce=True
                            )
                        ],className='border border-secondary rounded p-2 m-1')
                    ],width=4,)
                ]),
            ])
        ])
        # ,
        # # 社宅民眾
        # dbc.Row([
        #     dbc.Col([
        #         html.H3('社宅居民'),
        #         html.H5('民眾參與分析 權重'),
                
        #     ])
        # ])
    ])

# def tab_lower_adhesion(
#     score_weighted:list
# )->html.Div:
#     pass