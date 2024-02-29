from django.test import TestCase
from django.utils import timezone
from .models import Book, BookLoan, OnlineBook
from account.models import CustomUser

class LibraryModelsTestCase(TestCase):
    def setUp(self):
        # Test ma'lumotlari
        self.user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='parol')
        self.book = Book.objects.create(title='Test Kitob', author='Test Muallif', quantity=5, publication_year=2022)
        self.online_book = OnlineBook.objects.create(name='Test Onlayn Kitob', content='Test tarkibi', file='test.pdf')

    def test_book_creation(self):
        """Kitob modelini yaratishni tekshirish."""
        self.assertEqual(self.book.title, 'Test Kitob')
        self.assertEqual(self.book.author, 'Test Muallif')
        self.assertEqual(self.book.quantity, 5)
        self.assertEqual(self.book.publication_year, 2022)

    def test_bookloan_creation(self):
        """Kitob ijarasi modelini yaratishni tekshirish."""
        book_loan = BookLoan.objects.create(book=self.book, user=self.user, loan_date=timezone.now(), status='pending')
        self.assertEqual(book_loan.book, self.book)
        self.assertEqual(book_loan.user, self.user)
        self.assertEqual(book_loan.status, 'pending')

    def test_onlinebook_creation(self):
        """Onlayn kitob modelini yaratishni tekshirish."""
        self.assertEqual(self.online_book.name, 'Test Onlayn Kitob')
        self.assertEqual(self.online_book.content, 'Test tarkibi')
        self.assertEqual(self.online_book.file, 'test.pdf')

    def tearDown(self):
        # Test ma'lumotlarini tozalash
        self.user.delete()
        self.book.delete()
        self.online_book.delete()
