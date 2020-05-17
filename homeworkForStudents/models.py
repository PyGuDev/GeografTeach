from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class PersonModel(models.Model):
    CLASS_NUMBER = [
        ('5', '5 класс'),
        ('6', '6 класс'),
        ('7', '7 класс'),
        ('8', '8 класс'),
        ('9', '9 класс'),
        ('10', '10 класс'),
        ('11', '11 класс'),
    ]

    firstName = models.CharField("Имя", max_length=255, blank=False)
    lastName = models.CharField("Фамилия", max_length=255, blank=False)
    classNumber = models.CharField('Класс', max_length=255, choices=CLASS_NUMBER)

    verbose_name_plural = 'Ученик'
    verbose_name = 'Ученики'

    def __str__(self):
        return self.firstName
    

class TaskHomeWork(models.Model):
    title = models.CharField("Название", max_length=255, blank=False)
    task = RichTextUploadingField("Задание", blank=False)
    datePub = models.DateTimeField("Дата сдачи", auto_now=False, auto_now_add=False)

    verbose_name_plural = 'Задание'
    verbose_name = 'Задания'

    def __str__(self):
        return self.title
    

class AnswerTaskHomeWork(models.Model):
    ESTIMATION = [
        ('2', 'Неудовлетворительно'),
        ('3', 'Удовлетворительно'),
        ('4', 'Хорошо'),
        ('5', 'Отлично'),
    ]
    author = models.ForeignKey('PersonModel', on_delete=models.CASCADE)
    task = models.ForeignKey('TaskHomeWork', on_delete=models.CASCADE)
    answer = models.TextField('Ответ', default='', blank=False)
    img_answe = models.ImageField('Изображение', upload_to='media/answer/', blank=True)
    estimation = models.CharField('Оценка', max_length=255, choices=ESTIMATION)
    comment = models.TextField('Коментарий', blank=True)

    verbose_name_plural = 'Ответ'
    verbose_name = 'Ответы'
    
