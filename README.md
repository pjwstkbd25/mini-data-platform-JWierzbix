## Uruchamianie projektu:

1. Uruchom docker-compose 

`docker-compose up`

<u>Uruchomią się wtedy następujące serwisy:</u>

- **postgres**, dostępny na porcie `5432`. Ma on zmieniony tryb zapisywania informacji w logach o nowo dodanych danych. Potrzebne jest to do przechwytywania ich przez serwisk kafki.
- **zookeeper**, dostępny na porcie `2181`, który odpowiada za zarządzanie dystrybucją danych pomiędzy partycjami.
- **kafka**, dostępna na porcie `29092`, który odpowiada za przesyłanie danych w czasie rzeczywistym (streamowanie danych).
- **debezium**, dostępny na porcie `8083`, odpowiada za wykrywanie śledzenie, kiedy nowe dane w postgresie zostają dodane, po czym przekazuje te informacje do kafki.
- **debezium-connector-setup**, nadaje on automatyzację, gdyz odpowiada za tworzenie connectora pomiędzy debezium a postrgesem, od razu po utworzeniu serwisu debezium i postgres.
- **schema-registry**, dostępny na porcie `8081`, który odpowiada za przechowywanie i wersjonowanie schematów danych.
- **kafka-manager**, dostępny na porcie `9002`, który słuzy jako interfejs graficzny kafki. Jest on opcjonalnym serwisem i nie jesy potrzebny to poprawnego działania` serwisu.
- **minio**, dostępny na porcie `9000` jako serwer i `9001` jako serwer do Web UI. Słuzy on jako system rozproszony do przechowywania duzych plików i danych.
- **minio-init** serwis, który nadaje automatyzację, gdyz samodzielnie inicjalizuje bucket "streamed-data" do przechowywania danych przychodzących ze sparka.
- **spark**, dostępny na porcie `4040`, odpowiadający za przechwytywanie streamowanych danych z kafki, przetwarzanie ich oraz subskrybowanie ich do serwisu minio. Dodatkowo serwis ma przygotowany folder do przechowywania jobu, który uruchamia się za kazdym razem, gdy nowe dane zostaną przechwycone przez kafkę.

2. (opcjonalne) nawiąz połączenie kafka-managera z clustrem kafki.

3. Uruchom skrypt data_population_script.ipynb do inicjalizacji tabel w bazie, populacji danych do postgresa.

4. Uruchamiaj skrypt data_population_script.ipynb, aby imitować dodawanie nowych danych co jakiś czas. Obserwuj w volume minio jak dodawane są nowe commity z danymi.

5. W celu zamknięcia aplikacji uzyj:

6. W celu zamknięcia systemu uzyj komendy:

`docker-compose down`

Dla bezpieczeństwa dane są schowane w zmiennych środowiskowych, w pliku ".env".