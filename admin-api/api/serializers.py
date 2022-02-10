from rest_framework import serializers
from .models import Book, Member, BookLoaned


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['email', 'first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookLoanedSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(read_only=True, slug_field='email')
    class Meta:
        model = BookLoaned
        fields = ['user', 'book']


class UnAvailableBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLoaned
        fields = ['book', 'duration']
