from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()
    city = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=50, default='USA')

    def __str__(self):
        return self.name


class Book(models.Model):
    CATEGORY_CHOICES = [
        ('S', 'Science & Tech'),
        ('F', 'Fiction'),
        ('B', 'Biography'),
        ('T', 'Travel'),
        ('O', 'Other')
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default='S')
    num_pages = models.PositiveSmallIntegerField(default=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Member(User):
    STATUS_CHOICES = [
        (1, 'Regular Member'),
        (2, 'Premium Member'),
        (3, 'Guest Member'),
    ]

    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    address = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province = models.CharField(max_length=2, default='ON')
    last_renewal = models.DateField(default=timezone.now)
    auto_renew = models.BooleanField(default=True)
    borrowed_books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.username


class Order(models.Model):
    PURCHASE = 0
    BORROW = 1
    ORDER_TYPE_CHOICES = (
        (PURCHASE, 'Purchase'),
        (BORROW, 'Borrow'),
    )

    books = models.ManyToManyField(Book)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    order_type = models.IntegerField(choices=ORDER_TYPE_CHOICES, default=BORROW)
    order_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Order {self.id} by {self.member.username}"

    def total_items(self):
        return self.books.count()

