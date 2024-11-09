from datetime import datetime

day = datetime.now().strftime('%d')
month = datetime.now().strftime('%B')
year = datetime.now().strftime('%Y')

print(f'{day}.{month}.{year}')
