#Uruchamianie projektu:

1. Uruchom docker-compose 

'docker-compose up'

2. (opcjonalne) nawiąz połączenie kafka-managera z clustrem kafki.

3. Uruchom skrypt data_population_script.ipynb do inicjalizacji tabel w bazie, populacji danych do postgresa.

4. Uruchamiaj skrypt data_population_script.ipynb, aby imitować dodawanie nowych danych co jakiś czas. Obserwuj w volume minio jak dodawane są nowe commity z danymi.

5. W celu zamknięcia aplikacji uzyj:

6. W celu zamknięcia systemu uzyj komendy:

'docker-compose down'