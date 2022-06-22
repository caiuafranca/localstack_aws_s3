import boto3

endpoint_url = "http://localhost:4566"

client = boto3.client(
    "s3",
    endpoint_url=endpoint_url
)

arquivo = open('dados/entrada/teste2.txt', 'rb')

def upload():
    resposta = client.put_object(
        ACL='public-read-write',
        Bucket="my-bucket",
        Body=arquivo,
        Key="arquivo.csv"
    )
    resposta

def vizualizar():
    resposta = client.get_object(
        Bucket="my-bucket",
        Key="arquivo.csv"
    )
    print(resposta["Body"].read().decode('utf-8'))

def download():
    client.download_file("my-bucket","arquivo.csv","dados/saida/arquivo_download.csv")


upload()

download()