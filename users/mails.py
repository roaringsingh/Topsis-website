from django.core.mail import EmailMessage
import pandas as pd
from io import StringIO


def send_mail(file, obj):
    print(type(file))
    df = pd.read_csv(StringIO(file))
    mail = EmailMessage(
        'TOPSIS Result',
        f'Hello, {obj} \nPFA the result of the TOPSIS Analysis',
        'pymail26@gmail.com',
        [obj.email],
    )
    df.to_csv('temp/result.csv', index=False)
    mail.attach_file('temp/result.csv')
    mail.send()
    print('mail was sent')
    return
