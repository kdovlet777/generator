from django.db import models

class Question(models.Model):
	text = models.TextField('Text Of Question')
	generated = models.TextField('Generated Question')

class Email(models.Model):
	email = models.CharField('Email', max_length = 50)