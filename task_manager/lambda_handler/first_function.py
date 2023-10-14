import json
import random

def random_drink():
  drinks = ["coffee", "tea", "water", "juice"]
  return random.choice(drinks)

def lambda_handler(event, context):
    drink = random_drink()
    message = f"Yall should drink some {drink}"
    return {
        'statusCode': 200,
        'body': json.dumps({"message": message})
    }