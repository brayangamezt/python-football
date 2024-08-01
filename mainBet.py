from bets import Bets_methods
from htmlContent import get_html
import pdfkit
import time
import smtplib # Libreria para poder enviar emails
from email.message import EmailMessage
import os

api_key = '41e6acbc31cfc271dc03aea727ad4523'
api_host = 'v3.football.api-sports.io'
league_id = [39, 140, 262]
season = 2024
english_teams = [ 'chelsea', 'manchester city', 'manchester united', 'arsenal', 'liverpool', 'tottenham' ]
mexican_teams = [ 'cruz azul', 'club america', 'guadalajara chivas' ]
spain_teams = ['real madrid', 'barcelona']

if __name__ == '__main__':

    # Obtencion de los datos de las apuestas
    current_bet = Bets_methods( league_id, season, english_teams, mexican_teams, spain_teams, api_key, api_host )
    result = current_bet.final_results()

    text_html = get_html( result )
    with open( 'bets.html', 'a' ) as betsh:
        betsh.write( text_html )

    time.sleep( 4 )

    # Creacion del PDF
    options = {
        'no-stop-slow-scripts': None,
        'enable-local-file-access': None,
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
    pdfkit.from_file('bets.html', 'betWeek.pdf', configuration=config, options=options)

    # Envio del email
    email = 'bgtrujillo9@gmail.com'
    email_password = 'fhrjhqqdvgymklcq'
    destiny = 'bgamezt@outlook.com'
    destinies = ['bgamezt@outlook.com','bryanruelas09@gmail.com']

    send_email = EmailMessage()
    send_email['Subjet'] = 'Prueba asunto'
    send_email['From'] = email
    send_email['To'] = destinies
    send_email.set_content('Informacion de las apuestas de la semana')

    with open('betWeek.pdf', 'rb') as file_selected:
        file_data = file_selected.read()
        file_name = file_selected.name

    send_email.add_attachment( file_data, maintype='application', subtype='pdf', filename=file_name )


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, email_password)
        smtp.send_message(send_email)

    # Eliminar html y pdf creados
    os.remove( 'bets.html' )
    os.remove( 'betWeek.pdf' )