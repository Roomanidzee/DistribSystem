from django.db import models

# Create your models here.

class Message(models.Model):
    #сущность 'Сообщение'
    
    from_message = models.EmailField(max_length = 50, verbose_name = 'Отправитель')
    to_message = models.EmailField(max_length = 50, verbose_name = 'Получатель')
    topic = models.CharField(max_length = 100, verbose_name = 'Тема')
    message = models.CharField(max_length = 300, verbose_name = 'Сообщение')
    
    def __str__(self):
        
        return "From: {0}, to: {1}, topic: {2}\n, message: {3}\n".format(
            self.from_message, self.to_message, self.topic, self.message)
        
class Manager(models.Model):
    #сущность 'Менеджер'
    
    surname = models.CharField(max_length = 100, verbose_name = 'Фамилия')
    name = models.CharField(max_length = 100, verbose_name = 'Имя')
    patronymic = models.CharField(max_length = 100, verbose_name = 'Отчество')    
    work = models.CharField(max_length = 50, verbose_name = 'Специализация')
    
    def __str__(self):
        
        return "{0} {1} {2}, work: {3}".format(
            self.surname, self.name, self.patronymic, self.work)       
    