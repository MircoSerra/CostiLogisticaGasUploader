class Settings:
# Google settings
# Dall'account di Giacomo Telloli
    GOOGLE_ACCOUNTS_BASE_URL = 'https://accounts.google.com'
    REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
    GOOGLE_CLIENT_ID = '870015615971-662q25fvlj5juqts5ebviiqrl7kunboh.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = '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'
    GOOGLE_REFRESH_TOKEN = '1//09UzeAf31ERl_CgYIARAAGAkSNwF-L9Ir5lY088m4zDGavOHanWw5fZBoxInRC2E2xhFsjgc5joKha4AQX4QBW3VKN7uP2BoAzhw'

# Artesian setting
# Dall'account di Giacomo Telloli
    URL_SERVER = "https://arkive.artesian.cloud/K2E"
    API_KEY = "FtNKRBMUcnGlSchHwVCNXFkihqcr_zbi1eVCHu5-n2p7Ju0ZYkYCkFdAJronlhUoLjvzHeACcDmhcoZy1CSabZ9wBU5bFSYGhAwl-BS6kVlhe7khS2xjO5Nym_xykk8J"

# General settings
    csv_file = 'Generation.csv'
    CSV_OUTPUT_PATH = 'Y:\\Export CSVs\\'

# Plexos settings
    PLEXOS_PATH = "C:\Program Files\Energy Exemplar\PLEXOS 8.3"
    SOLUTION_FILE = "Y:\\Plexos\\Archivio simulazioni\\Dispacciamento Servola\\Storico\\2022\\February\\04\\14\\Project con e senza vincoli Solution\\Project con e senza vincoli Solution.zip"
    # Plexos solution parameters
    SOLUTION_NAMES = ['Generator', 'Fuel', 'Emission', 'Region']
    GENERATORS_PROPERTY = '1,5,13,14,80,84,91,93,94,96,133,182,198'
    FUELS_PROPERTY = '1,2,5'
    CO2_PROPERTY = '1,9'
    PRICE_PROPERTY = '60'
    LIST_OF_COLLECTION = [1, 19, 31, 240]
    LIST_OF_PROPERY = [
        GENERATORS_PROPERTY,
        FUELS_PROPERTY,
        CO2_PROPERTY,
        PRICE_PROPERTY
    ]
    STRING_OF_INTERVAL_START = '01/12/2021'
    STRING_OF_INTERVAL_END = '31/12/2024'
    INT_START_YEAR = 2022
    INT_END_YEAR = 2024
    INT_START_MONTH = 1
    INT_END_MONTH = 12

# Dataframe settings
    LIST_OF_COLUMNS_NAMES = [
        # Nomi delle colonne del dataframe "Generator"
        ['model_name', 'collection_name', 'child_name', 'date',
            'Generation (MW)', 'Units Started', 'Fuel Offtake (MWht)',
            'Start Fuel Offtake (MWht)', 'Fuel Cost (€)', 'VO&M Cost (€)',
            'Start & Shutdown Cost (€)', 'Start Fuel Cost (€)',
            'Emissions Cost (€)', 'Total Generation Cost (€)', 'Pool Revenue (€)',
            'Installed Capacity (MW)', 'Available Capacity (MW)'],
        # Nomi delle colonne del dataframe "Fuel"
        ['model_name', 'collection_name', 'child_name', 'date', 'Price (€/MWht)',
            'Tax (€/MWht)', 'Offtake (MWht)'],
        # Nomi delle colonne del dataframe "Emissions"
        ['model_name', 'collection_name', 'child_name', 'date', 'Production (t)',
            'Price (€/t)'],
        # Nomi delle colonne del dataframe "Region"
        ['model_name', 'collection_name', 'child_name', 'date', 'Price (€/MWh)']
    ]
    LIST_COLLECTION_NAME_CHILD_NAME = [
        # Child name e Collection name per il dataframe "Generator"
        ('Generator', 'Servola_new'),
        # Child name e Collection name per il dataframe "Fuel"
        ('Fuel', 'PSV'),
        # Child name e Collection name per il dataframe "Emissions"
        ('Emission', 'CO2'),
        # Child name e Collection name per il dataframe "Price"
        ('Region', 'NORD')
    ]
# Ore di picco e baseload settings
    INIZO_ORE_DI_PICCO = 8
    FINE_ORE_DI_PICCO = 19
    SABATO = 5
    DOMENICA = 6

# Costanti generali
    RENDIMENTO_GAS = 0.5
    COEFFICIENTE_EMISSIVO = 0.4
    COEFFICIENTE_CONVERSIONE_PCI_PCS = 0.901
    COSTI_LOGISTICA_GAS_VARIABILI = 1.85

# Artesian curve name setting
    dict_of_names = {
        'Offtake': 'Volume',
        'Ton co2': 'Volume',
        'Generation' : 'Volume',
        'Generation (MW)': 'Volume',
        'Units Started': 'Units Started',
        'Fuel Offtake (MWht)': 'Volume',
        'Start Fuel Offtake (MWht)': 'Volume',
        'Fuel Cost (€)': 'Costo',
        'VO&M Cost (€)': 'Costo',
        'Start & Shutdown Cost (€)': 'Costo',
        'Start Fuel Cost (€)': 'Costo',
        'Price (€/t)': 'Costo',
        'Total Generation Cost (€)': 'Costo',
        'Pool Revenue (€)': 'Ricavi',
        'Installed Capacity (MW)': 'Volume',
        'Available Capacity (MW)': 'Volume',
        'Tax (€/MWht)': 'Prezzo',
        'Offtake (MWht)': 'Volume',
        'Smc gas': 'Volume',
        'Ton CO2': 'Volume',
        'Production (t)': 'Volume',
        'P&L': 'Risultato operativo',
        'EUA': 'Prezzo',
        'CV 50%': 'Ricavo',
        'media MW pk': 'Volume',
        'media MW off': 'Volume',
        'media MW gas consumati': 'Volume',
        'CSS BS 50% pcs': 'Prezzo',
        'CSS PK 50% pcs': 'Prezzo',
        'CSS BS 50% pci': 'Prezzo',
        'CSS PK 50% pci': 'Prezzo',
        'Price (€/MWh)': 'Mixed Pun-Nord'
    }

    dict_of_typologies ={
        'Generator': 'Power',
        'Fuel': 'Gas',
        'Emission': 'Co2',
        'Region': 'Prezzo'
    }

