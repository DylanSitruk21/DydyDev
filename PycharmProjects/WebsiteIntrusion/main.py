import requests
from bs4 import BeautifulSoup as bs
import openpyxl

# url = 'https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal'
# # values = {'id': 'dylansitruk@hotmail.fr',
# #           'method': '@'}
#
# r = requests.post(url)  # , data=values)
# soup = bs(r.content, "html.parser")
#
# # print(soup.title.get_text())
# # print(soup.get_text())
# # print(soup.prettify())
# # print(soup.find_all("a"))
# # print(soup.get_text())

########################

# Effectuer une requête pour se connecter
login_url = 'https://services.cal-online.co.il/Card-Holders/Screens/AccountManagement/Login.aspx?ReturnUrl=%2fCard-Holders%2fSCREENS%2fAccountManagement%2fHomePage.aspx'
credentials = {
    'username': 'votre_nom_d_utilisateur',
    'password': 'votre_mot_de_passe'
}
response = requests.post(login_url, data=credentials)

# Vérifier l'état de la connexion
if response.status_code == 200:
    # Accéder à la page des transactions
    transactions_url = 'https://services.cal-online.co.il/Card-Holders/Screens/Transactions/Transactions.aspx'
    response = requests.get(transactions_url)

    # Analyser le contenu de la page
    soup = bs(response.content, 'html.parser')

    # Extraire les informations des transactions
    transactions = []
    transaction_elements = soup.find_all('div', class_='transaction')
    for transaction_element in transaction_elements:
        date = transaction_element.find('span', class_='date').text
        amount = transaction_element.find('span', class_='amount').text
        beneficiary = transaction_element.find('span', class_='beneficiary').text
        transactions.append({
            'date': date,
            'amount': amount,
            'beneficiary': beneficiary
        })

    # Écrire les données dans un fichier Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(['Date', 'Montant', 'Bénéficiaire'])
    for transaction in transactions:
        sheet.append([transaction['date'], transaction['amount'], transaction['beneficiary']])

    workbook.save('transactions.xlsx')
else:
    print('Échec de la connexion.')


