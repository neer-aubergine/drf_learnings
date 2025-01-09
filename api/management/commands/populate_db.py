# from django.core.management.base import BaseCommand
# from faker import Faker
# from api.models import User, Product

# class Command(BaseCommand):
#     help = 'Populate the database with sample data'

#     def handle(self, *args, **kwargs):
#         fake = Faker()

#         # Create sample users
#         for _ in range(10):
#             User.objects.create_user(
#                 username=fake.user_name(),
#                 password='password'
#             )

#         # Create sample products
#         for _ in range(10):
#             Product.objects.create(
#                 name=fake.word(),
#                 price=fake.pydecimal(left_digits=4, right_digits=2, positive=True),
#                 description=fake.text(),
#                 stock=fake.random_int(min=0, max=100)
#             )

#         self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data'))




from django.core.management.base import BaseCommand
from faker import Faker
from api.models import User, Product, Order, OrderItem

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create sample users
        users = []
        for _ in range(10):
            user = User.objects.create_user(
                username=fake.user_name(),
                password='password'
            )
            users.append(user)

        # Create sample products
        products = []
        for _ in range(10):
            product = Product.objects.create(
                name=fake.word(),
                price=fake.pydecimal(left_digits=4, right_digits=2, positive=True),
                description=fake.text(),
                stock=fake.random_int(min=0, max=100)
            )
            products.append(product)

        # Create sample orders
        for _ in range(10):
            order = Order.objects.create(
                user=fake.random_element(elements=users)
            )

            # Create sample order items
            for _ in range(fake.random_int(min=1, max=5)):
                OrderItem.objects.create(
                    order=order,
                    product=fake.random_element(elements=products),
                    quantity=fake.random_int(min=1, max=10)
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data'))