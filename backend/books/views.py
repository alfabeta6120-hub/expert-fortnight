from .models import Author,Genre,BookType,Book
from rest_framework import serializers

"""Создаем Сериализацию для Модели Author"""
class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author 
        # передаем атрибуты модели
        fields = [ 'id','name','year_of_birth','bio','country']
        
        
"""Создаем Сериализацию для Модели Genre"""
class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre 
        #  передаем атрибуты модели
        fields = ['id','title']
        
"""Создаем Сериализацию для Модели BookType"""
class BookTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookType
        #  передаем атрибуты модели
        fields = ['id','book_type']
        
"""Создаем Сериализацию для Модели Book"""
class BookSerializer(serializers.ModelSerializer):
    # Автор
    author = AuthorSerializer(read_only=True)
    # Жанр
    genre = GenreSerializer(read_only=True)
    # тип книги
    book_type = BookTypeSerializer(read_only=True)
    
    class Meta:
        model = Book
        #  передаем атрибуты модели
        fields = ['id','author','genre','book_type']
        
        