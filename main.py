from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/Users/chasepreston/PycharmProjects/chromedriver')
driver.get('https://www.jetpunk.com/quizzes/how-many-countries-can-you-name')

start_button = driver.find_element(By.ID, 'start-button')
start_button.click()

txt_answer_box = driver.find_element(By.ID, 'txt-answer-box')

countries = [
    # North America
    'Antigua', 'Bahamas', 'Barbados', 'Belize', 'Canada', 'Costa Rica', 'Cuba', 'DR', 'Dominica', 'El Salvador',
    'Grenada', 'Guatemala', 'Haiti', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Saint Kitts',
    'Saint Lucia', 'Saint Vincent', 'Trinidad', 'USA',
    # South America
    'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname',
    'Uruguay', 'Venezuela',
    # Europe
    'Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark',
    'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia',
    'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands',
    'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia',
    'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'UK', 'Ukraine', 'Vatican',
    # Asia
    'Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'Cyprus',
    'East Timor', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait',
    'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan',
    'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan',
    'Thailand', 'Turkey', 'Turkmenistan', 'UAE', 'Uzbekistan', 'Vietnam', 'Yemen', 'Maldives',
    # Africa
    'Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde', 'CAR', 'Chad',
    'Comoros', 'DRC', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia',
    'Ghana', 'Guinea', 'Guinea Bissau', 'Ivory Coast', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi',
    'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Congo', 'Rwanda',
    'Sao Tome', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania',
    'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe',
    # Oceania
    'Australia', 'Micronesia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Nauru', 'New Zealand', 'Palau',
    'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu'
]

for country in countries:
    txt_answer_box.send_keys(country)