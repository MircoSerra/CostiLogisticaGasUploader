import datetime as dt
import pandas as pd
import time
from dateutil.easter import *
from dateutil.rrule import rrule, HOURLY

import settings_and_imports as setting


def find_off_peak_hours(df, month, year):
    df_off_peak = df.loc[((df['date'].dt.hour < setting.Settings.INIZO_ORE_DI_PICCO) |
                          (df['date'].dt.hour > setting.Settings.FINE_ORE_DI_PICCO) |
                          ((df['date'].dt.day_of_week == setting.Settings.SABATO) |
                           (df['date'].dt.day_of_week == setting.Settings.DOMENICA))) &
                         ((df['date'].dt.month == month) &
                          (df['date'].dt.year == year))]
    return df_off_peak


def find_peak_hours(df, month, year):
    df_peak = df.loc[
        (df['date'].dt.hour > setting.Settings.INIZO_ORE_DI_PICCO - 1) &
        (df['date'].dt.hour < setting.Settings.FINE_ORE_DI_PICCO + 1) &
        (df['date'].dt.day_of_week != setting.Settings.SABATO) &
        (df['date'].dt.day_of_week != setting.Settings.DOMENICA) &
        (df['date'].dt.month == month) &
        (df['date'].dt.year == year)
        ]
    return df_peak


def find_easter(year):
    pasqua = easter(year)
    return pasqua


# Compara due date sino all'ordine del giorno, rendendo True se sono uguali,
# -1 se d2 è maggiore di d1 e +1 se d1 è maggiore di d2
def compare_date(d1, d2):
    # Controllo se l'anno è lo stesso
    if d1.year == d2.year:
        # Controllo se il mese è lo stesso
        if d1.month == d2.month:
            # Controllo se il giorno è lo stesso
            if d1.day == d2.day:
                # Se è tutto vero rendo True
                return True
            else:
                if d1.day > d2.day:
                    return +1
                else:
                    return -1
        else:
            if d1.month > d2.month:
                return +1
            else:
                return -1
    else:
        if d1.year > d2.year:
            return +1
        else:
            return -1


# Compara due date sino all'ordine del giorno, rendendo 0 se sono uguali,
# -1 se d2 è maggiore di d1 e True se d1 è maggiore di d2
def compare_date_maggiore(d1, d2):
    # Controllo se l'anno è lo stesso
    if d1.year == d2.year:
        # Controllo se il mese è lo stesso
        if d1.month == d2.month:
            # Controllo se il giorno è lo stesso
            if d1.day == d2.day:
                # Se è tutto vero rendo True
                return 0
            else:
                if d1.day > d2.day:
                    return True
                else:
                    return -1
        else:
            if d1.month > d2.month:
                return True
            else:
                return -1
    else:
        if d1.year > d2.year:
            return True
        else:
            return -1


# Compara due date sino all'ordine del giorno, rendendo 0 se sono uguali,
# True se d2 è maggiore di d1 e +1 se d1 è maggiore di d2
def compare_date_minore(d1, d2):
    # Controllo se l'anno è lo stesso
    if d1.year == d2.year:
        # Controllo se il mese è lo stesso
        if d1.month == d2.month:
            # Controllo se il giorno è lo stesso
            if d1.day == d2.day:
                # Se è tutto vero rendo True
                return 0
            else:
                if d1.day > d2.day:
                    return +1
                else:
                    return True
        else:
            if d1.month > d2.month:
                return +1
            else:
                return True
    else:
        if d1.year > d2.year:
            return +1
        else:
            return True


# Mi dice se un Timestamp cade in ora di picco di un giorno generico senza considerare festività
def is_peak_time(timestamp_hours):
    # Controllo se l'orario cade tra le ore otto e le ore venti, controllo anche che il giorno della settimana non sia
    # ne sabato ne tanto meno domenica.
    return ((
                (timestamp_hours.hour > setting.Settings.INIZO_ORE_DI_PICCO - 1) &
                (timestamp_hours.hour < setting.Settings.FINE_ORE_DI_PICCO + 1)
            )
            &
            (
                (timestamp_hours.day_of_week != setting.Settings.SABATO) &
                (timestamp_hours.day_of_week != setting.Settings.DOMENICA))
            )


# Mi dice se un Timestamp (data e ora) è ora di picco o fuori picco considerando anche le feste nazionali
def is_peak(timestamp_hours):
    return is_peak_time(timestamp_hours)


def is_peak_with_festivita(timestamp_hours):
    # Recupero la data della domenica di Pasqua
    pasqua = find_easter(timestamp_hours.year)
    # Aggiungo un giorno per ottenere il lunedì di Pasquetta
    pasqua = pd.Timestamp(pasqua) + dt.timedelta(days=1)
    # Imposto la data di ferragosto
    ferragosto = dt.datetime(timestamp_hours.year, 8, 15)
    # Imposto la data di ogni santi
    ognisanti = dt.datetime(timestamp_hours.year, 11, 1)
    # Imposto la data della befana
    befana = dt.datetime(timestamp_hours.year, 1, 6)
    # Imposto la data della festa dei lavoratori
    festa_lavoratori = dt.datetime(timestamp_hours.year, 5, 1)
    # Imposto la data della festa della repubblica
    festa_della_repubblica = dt.datetime(timestamp_hours.year, 6, 2)
    # Imposto la data di Natale
    natale = dt.datetime(timestamp_hours.year, 12, 25)
    # Imposto la data della vigilia di Natale
    vigilia_di_natale = dt.datetime(timestamp_hours.year, 12, 24)
    # Imposto la data di santo Stefano
    santo_stefano = dt.datetime(timestamp_hours.year, 12, 26)
    # Imposto la data della festa della liberazione
    festa_della_liberazione = dt.datetime(timestamp_hours.year, 4, 25)
    # Controllo che la data e l'ora in esame cadano nelle ore di picco e in nessun giorno di festa nazionale
    return is_peak_time(timestamp_hours) & (not compare_date(timestamp_hours, pasqua)) &\
          (not compare_date(timestamp_hours, ferragosto)) &\
          (not compare_date(timestamp_hours, ognisanti)) &\
          (not compare_date(timestamp_hours, befana)) &\
          (not compare_date(timestamp_hours, festa_lavoratori)) &\
          (not compare_date(timestamp_hours, festa_della_repubblica)) &\
          (not compare_date(timestamp_hours, natale)) &\
          (not compare_date(timestamp_hours, vigilia_di_natale)) &\
          (not compare_date(timestamp_hours, santo_stefano)) &\
          (not compare_date(timestamp_hours, festa_della_liberazione))


# Date due date in formato Timestamp, rende due liste di ore, la prima contenente
# le ore di picco, la seconda contenente le ore fuori picco
def find_peak_hours_on_interval(timestamp_primo_estremo, timestamp_secondo_estremo):
    lista_ore_di_picco = list()  # Inizializzo le due liste che conterranno i risultati
    lista_ore_fuori_picco = list()
    # Questo ciclo mi permette di scorrere le ore comprese tra i due intervalli di time stamp
    for ax in rrule(HOURLY, dtstart=timestamp_primo_estremo, until=timestamp_secondo_estremo):
        # Converto la data e l'ora fornite dalla funzione "ciclante" in timestamp
        ax = pd.Timestamp(ax)
        # Controllo se sia un ora di picco o meno
        if is_peak(ax):
            # Assegno alla lista corretta
            lista_ore_di_picco.append(ax)
        else:
            # Assegno alla lista corretta
            lista_ore_fuori_picco.append(ax)

        return lista_ore_di_picco, lista_ore_fuori_picco


# Data una data formattata come stringa, e la sua formattazione, la converte in Datetime di pandas
def string_to_datetime(stringa, formato=''):
    x = pd.to_datetime(stringa, format=formato)
    return x


# Data una data formattata come stringa, e la sua formattazione, rende due liste di ore, la prima contenente
# le ore di picco, la seconda contenente le ore fuori picco
def find_peak_n_off_peak_hours_on_interval(string_start, string_end, date_format):
    lista_ore_di_picco = list()  # Inizializzo le due liste che conterranno i risultati
    lista_ore_fuori_picco = list()
    # Converto la data d'inizio intervallo in datetime
    start = string_to_datetime(string_start, formato=date_format)
    # Converto la data di fine intervallo in datetime
    end = string_to_datetime(string_end, formato=date_format)
    # Questo ciclo mi permette di scorrere le ore comprese tra i due intervalli di time stamp
    for ax in rrule(HOURLY, dtstart=start, until=end):
        # Converto la data e l'ora fornite dalla funzione "ciclante" in timestamp
        ax = pd.Timestamp(ax)
        # Controllo se sia un ora di picco o meno
        if is_peak(ax):
            # Assegno alla lista corretta
            lista_ore_di_picco.append(ax)
        else:
            # Assegno alla lista corretta
            lista_ore_fuori_picco.append(ax)
    return lista_ore_di_picco, lista_ore_fuori_picco


# Rende solamente le tuple di un dataframe che rientrano un dato intervallo temporale
def get_interval(df, string_inizio, string_fine, string_format):
    # Converto le date da stringa in formato datetime
    dt_inizio = string_to_datetime(string_inizio, formato=string_format)
    dt_fine = string_to_datetime(string_fine, formato=string_format)
    # Taglio il dataframe per anno
    df_result = df.loc[(df['date'].dt.year <= dt_fine.year) & (df['date'].dt.year >= dt_inizio.year)]
    # Taglio il dataframe per mese
    df_result = df_result.loc[
        (df_result['date'].dt.month <= dt_fine.month) & (df_result['date'].dt.month >= dt_inizio.month)]
    # Taglio il dataframe per giorno
    df_result = df_result.loc[(df_result['date'].dt.day <= dt_fine.day) & (df_result['date'].dt.day > dt_inizio.day)]

    return df_result


def format_date(data):
    return data.to_pydatetime()


def get_hours_between_dates(str_start, str_stop):
    return pd.date_range(str_start, str_stop, freq='H')


def str_dt_date_time_to_utc(dt_date_time, str_output_format):
    return dt.datetime.utcfromtimestamp(dt_date_time.timestamp()).strftime(str_output_format)

"""
Cronometer class useful for check the execution
time of functions in any Python code
"""


class ChronoMeter:
    # properties
    start_time = 0
    end_time = 0

    """
    Method to start the cronometer
    """

    def start_chrono(self):
        self.start_time = self.current_milli_time()

    """
    Method for stopping chronometer
    """

    def stop_chrono(self):
        self.end_time = self.current_milli_time()

    """
    Method that return the execution time,
    the difference between end time and
    start time
    """

    def get_execution_time(self):
        return self.end_time - self.start_time

    """
    Method that print the execution time
    """

    def print_time(self):
        print(f"execution time: {self.get_execution_time()} ms")

    """
    Method that return the current time in 
    milliseconds
    """

    def current_milli_time(self):
        return round(time.time() * 1000)