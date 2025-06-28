echo 'Waiting for Kafka Connect to be ready...'
until curl -f http://debezium:8083/connectors; do
    echo 'Kafka Connect is not ready yet. Waiting...'
    sleep 5
done

echo 'Kafka Connect is ready. Registering connector...'

curl -X POST http://debezium:8083/connectors/ \
    -H 'Content-Type: application/json' \
    -d @/app/debezium-connector-config.json
echo 'Connector registration completed.'