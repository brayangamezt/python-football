def get_html(data):

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="./main.css">
        <title>Tabla</title>
    </head>
    <body>
        <div class="main-container" >
    """

    for game in data:
        html += f"""
        <div class="game" >
            <h3 class="title-game"> { game['local']['local_team_name'] } vs { game['away']['away_team_name'] } </h3>
            <p class="advice" > Prediccion: { game['advice'] } </p>
            <br>
            <p class="comment-percent" > Porsentaje de victoria </p>
            <div class="percent" >
                <div class="home" >Loca: { game['victory']['home'] }</div>
                <div class="draw" >Empate: { game['victory']['draw'] }</div>
                <div class="away" >Visitante: { game['victory']['away'] }</div>
            </div>
            <div class="teams-information" >
                <div class="local-team" >
                    <h4> { game['local']['local_team_name'] } </h4>
                    <p> <strong> Ultimos 5 juegos: </strong>                 { game['local']['local_last_5_games_gols'] }</p>
                    <p> <strong> Promedio ultimos 5 juegos: </strong>        { game['local']['local_average_last_5_games'] }</p>
                    <p> <strong> Victorias equipo local:</strong>            { game['local']['home_team_wins'] }</p>
                    <p> <strong> Empates equipo local:</strong>              { game['local']['home_team_draws'] }</p>
                    <p> <strong>Derrotas equipo local:</strong>              { game['local']['home_team_loses'] }</p>
                    <p> <strong>Goles como local: </strong>                  { game['local']['home_team_goals_for'] } </p>
                    <p> <strong>Goles como visitante:</strong>               { game['local']['home_team_goals_against'] }</p>
                    <p> <strong>Goles a favor por minuto PT:</strong>        { game['local']['home_team_goals_for_first_half'] }</p>
                    <p> <strong>Goles a favor por minuto ST:</strong>        { game['local']['home_team_goals_for_second_half'] } </p>
                    <p> <strong>Goles en contra por minuto PT: </strong>     { game['local']['home_team_away_against_goals_FH'] }</p>
                    <p> <strong>Goles en contra por minuto ST: </strong>     { game['local']['home_team_away_against_goals_SH'] }</p>
                </div>
                <div class="away-team" >
                    <h4> { game['away']['away_team_name'] } </h4>
                    <p> <strong> Victorias equipo local:</strong>            { game['away']['away_team_wins'] }</p>
                    <p> <strong> Empates equipo local:</strong>              { game['away']['away_team_draws'] }</p>
                    <p> <strong>Derrotas equipo local:</strong>              { game['away']['away_team_loses'] }</p>
                    <p> <strong>Goles como local: </strong>                  { game['away']['away_team_goals_for'] }</p>
                    <p> <strong>Goles como visitante:</strong>               { game['away']['away_team_goals_against'] }</p>
                    <p> <strong>Goles a favor por minuto PT:</strong>        { game['away']['away_team_goals_for_FH'] } </p>
                    <p> <strong>Goles a favor por minuto ST:</strong>        { game['away']['away_team_goals_for_SH'] } </p>
                    <p> <strong>Goles en contra por minuto PT: </strong>     { game['away']['away_team_goals_against_FH'] }</p>
                    <p> <strong>Goles en contra por minuto ST: </strong>     { game['away']['away_team_goals_against_SH'] }</p>
                </div>
            </div>
        </div>
        """
    html += f"""
        </div>
    </body>
    </html>
    """

    return html
