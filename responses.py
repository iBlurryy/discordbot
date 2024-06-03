import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'test123':
        return 'working'
    
    if message == 'roll a dice':
        return str(random.randint(1,6))
    
    if p_message == '!help':
        return '`Commands - !help, test123, roll a dice`'
    

    return 'Sorry, I didn\'t understand. Try typing !help.'