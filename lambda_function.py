import json
import boto3

# DynamoDB bağlantısı
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('KamyonVerileri')

def lambda_handler(event, context):
    try:
        # 1. Gelen veriyi (index.pydan gelen) oku
        body = json.loads(event['body'])
        hiz = body.get('hiz', 0)
        
        if hiz > 110:
            body['analiz_sonucu'] = "TEHLIKELI - YUKSEK HIZ"
            body['alarm_durumu'] = True
        else:
            body['analiz_sonucu'] = "NORMAL"
            body['alarm_durumu'] = False
            
        
        table.put_item(Item=body)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'mesaj': 'Veri analiz edildi ve kaydedildi!',
                'tespit_edilen_durum': body['analiz_sonucu']
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Hata: {str(e)}")
        }