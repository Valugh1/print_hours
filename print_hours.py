import datetime as dt 
import calendar as c
from icecream import ic

# Ottenere la data e ora correnti
now = dt.datetime.now()
#ts_now = dt.datetime.timestamp(now)

# Impostare la data al primo giorno del mese corrente
start_of_month = dt.datetime(now.year, now.month, 1)

# Ottenere l'ultimo giorno del mese corrente
_, last_day = c.monthrange(now.year, now.month)

# Generare tutte le ore del mese corrente
curr_month_hours = []
for day in range(1, last_day + 1):
    for hour in range(24):
        current_datetime = dt.datetime(now.year, now.month, day, hour)
        ts_current_datetime = dt.datetime.timestamp(current_datetime)
        curr_month_hours.append(current_datetime)



# Cerco il primo giorno della settimana
my_dt_trunc = now.date()
start_of_week = now - dt.timedelta(days=now.weekday())
start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
#ts_start_of_week = int(start_of_week.timestamp())


# Cerco l'ultimo giorno della settimana
end_of_week = start_of_week + dt.timedelta(days = 7)
#ts_end_of_week = int(end_of_week.timestamp())

# Filtrare le ore eliminando la settimana corrente e stampo solo le ore comprese tra le 9 e le 19
filtered_hours = []
for hour in curr_month_hours:
    if not (start_of_week < hour < end_of_week):
        if 9 <= hour.hour <= 19:

            filtered_hours.append(hour.strftime("%A %d  %b, %Y __ ora: %H:%M"))

ic(filtered_hours)
