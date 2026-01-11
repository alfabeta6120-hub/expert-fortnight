from django.db import models

"""Создаем модель Author (Автор) и берем импорт из Базы данных Django"""
class Author(models.Model):
    
    """Передаем стандартные атрибуты"""
    # имя
    name = models.CharField(max_length=20)
    # год рождения
    year_of_birth = models.CharField(max_length=10)
    # биография
    biography = models.TextField(blank=True)
    # страна
    country = models.CharField(max_length=15)
    
    """Передаем магический метод str"""
    def __str__(self) -> str:
        return self.name
    
       
"""Создаем Модель Genre (жанр книги)"""  
class Genre(models.Model):
    
    # заголовок жанра книги
<<<<<<< Updated upstream
    title = models.CharField(max_length=20,choices=[
        ('the class','классика'),
        ('drama','драма' ),
        ('comedi','комедия'),
        ('fantastic','фантастика'),
    ])
=======
    title = models.CharField(max_length=50)
>>>>>>> Stashed changes
    
    """Передаем магический метод str"""
    def __str__(self) -> str:
        return self.title
    
    
"""Создаем Модель BookType(Тип книги)""" 
class  BookType(models.Model):
    
    # тип книги
    book_type = models.CharField(max_length=True)

    
    """Передаем магический метод str"""   
    def __str__(self) -> str:
         return self.book_type 
      

"""Создаем Модель Book(книга)"""
class Book(models.Model):
    
    # Заголовок книги
    title = models.CharField(max_length=20)
    
    """Передаем атрибуты передаются по первичному ключу"""
    # Тип книги
    book_type = models.ManyToManyField(BookType,blank=True)
    # Автор
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    # Жанр
    genre = models.ManyToManyField(Genre,blank=True)
    
    """Передаем магический метод str"""
    def __str__(self) -> str:
        return self.title
    
    
    