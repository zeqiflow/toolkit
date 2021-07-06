python fate_flow_client.py -f upload -c homo_examples/upload_$2.json

sleep 10s

echo "Table $2 info:"

python fate_flow_client.py -f table_info -n experiment_$2 -t $1_$2
