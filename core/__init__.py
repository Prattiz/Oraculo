import datetime


class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = f'São {now.hour} horas e {now.minute} minutos.' # change into -- its {} hours and {} minutes --
        return answer
    
    @staticmethod
    def get_date():
        now = datetime.datetime.now()
        answer = 'Hoje é dia {} de {} de {}'.format(now.day, now.strftime('%B'), now.year)

        return answer