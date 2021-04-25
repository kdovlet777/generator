from django.shortcuts import render
from .models import Question, Email
from django.contrib import messages
from django.core.mail import send_mail
import random

def index(request):
	if request.method == 'POST':
		Question.objects.all().delete()
		question = Question.objects.create(text = request.POST['text'])
		s = question.text
		global fin_string
		fin_string = ''
		s1 = s[s.find('a='):]
		ans_a = s1[2:s1.find(' ')]


		s3 = s[s.find('b='):]
		ans_b = s3[2:s3.find(' ')]


		s2 = s[s.find('c='):]
		ans_c = s2[2:s2.find(' ')]


		if ans_a and ans_b:
			for _ in range(10):
				b = random.randint(5,30)*10
				c = random.randint(2, 15)
				while(b % c!=0):
					c = random.randint(2,15)
				rep_string = s.replace(f'a={ans_a}',str(int(b/c)))
				rep_string = rep_string.replace(f'b={ans_b}', str(b))
				rep_string += f' Ответ: {c}'
				fin_string += rep_string + '\n'
			question.generated = fin_string
			

		if ans_a and ans_c:
			for _ in range(10):
				b = random.randint(5,30)*10
				c = random.randint(2,20)
				while(b % c!=0):
					c = random.randint(2,20)
				rep_string = s.replace(f'a={ans_a}', str(int(b/c)))
				rep_string = rep_string.replace(f'c={ans_c}', str(c))
				rep_string += f' Ответ: {b}'
				fin_string += rep_string + '\n'
			question.generated = fin_string	


		if ans_b and ans_c:
			for _ in range(10):
				b = random.randint(5,30)*10
				c = random.randint(2, 15)
				while(b % c!=0):
					c = random.randint(2,15)
				rep_string = s.replace(f'c={ans_c}',str(c))
				rep_string = rep_string.replace(f'b={ans_b}', str(b))
				rep_string += f' Ответ: {int(b/c)}'
				fin_string += rep_string + '\n'
			question.generated = fin_string
		question.save()
		return render(request, 'base.html', {'question':question})
	else:
		return render(request, 'base.html')

def panel(request):
	if request.method == 'POST':
		email = Email.objects.create(email = request.POST['email'])
		created = email.email
		email.save()
		messages.info(request, f'Почта {created} добавлена успешно!')
	emails_list = Email.objects.all()
	emails_count = emails_list.count()
	return render(request, 'panel.html', {'emails_list':emails_list, 'emails_count':emails_count})

def delete(request, email_id):
	deleted = Email.objects.get(id = email_id)
	Email.objects.filter(id=email_id).delete()
	emails_list = Email.objects.all()
	messages.info(request, f'Почта {deleted.email} удалена успешно!')
	return render(request, 'panel.html', {'emails_list':emails_list})

def send_mails(request):
	i = 0
	q_array = []
	e_array = []
	emails_list = Email.objects.all()
	emails_count = emails_list.count()
	question_set = fin_string
	for q in question_set.split('\n'):
		q = q[:q.find('?')+1]
		q_array.append(q)
	for e in emails_list:
		e_array.append(e.email)
	for i in range(emails_count):
		send_mail(
	    'Домашнее задание',
	    q_array[i],
	    'sjobs2901@gmail.com',
	    [e_array[i]],
	    fail_silently=False,
		)
	messages.info(request, 'Все задачи успешны отправлены на почты')
	return render(request, 'base.html')

