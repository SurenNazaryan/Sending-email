import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

login = os.getenv('login')
password = os.getenv('password')

letter = f"""From: nazaryan_suren@bk.ru
To: suren-nazaryan_228@mail.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";


Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".replace('%website%','https://dvmn.org/profession-ref-program/skyephirts/uzo2M/').replace('%friend_name%', 'Сурен').replace('%my_name%', 'Сурен')

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.mail.ru:465')
server.login(login, password)
server.sendmail('nazaryan_suren@bk.ru','suren-nazaryan228@mail.ru', letter)
server.quit()

website = 'https://dvmn.org/profession-ref-program/skyephirts/uzo2M/'
friend_name = 'Сурен'
my_name = 'Сурен'
new_letter = f'''Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website} 
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''


