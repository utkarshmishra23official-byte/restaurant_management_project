python manage.py shell

from django.contrib.auth.models import User
from restaurant.models import MenuItem, Order, OrderItem

user = User.objects.first()
item1 = MenuItem.objects.first()

#create order
order = Order.objects.create(customer=user, total_amount=0)

#add item
OrderItem.objects.create(order=order, menu_item=item1, quantity=2)

#update total
order.total_amount = item1.price * 2
order.save()