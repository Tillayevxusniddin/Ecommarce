from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from products.models import Order, Product


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'product', 'customer', 'quantity', 'created_at', 'total_price', 'phone_number']


    def get_total_price(self, obj):   #narxni miqdorga kopaytirib umumiy summani chiqaramiz METHODFIELD bolgani uchun total_pricega ulangan
        return obj.product.price * obj.quantity

    def validate_quantity(self, value):
        try:
            product_id = self.initial_data['product']  #productni idsini olamiz
            product = Product.objects.get(id=product_id)  #va Bazadan idga qarab productni olamiz

            if value > product.stock:  #soralgan qiymat katta bolsa stockdan uncha mahsulot yoq deymiz
                raise serializers.ValidationError("Not enough items in stock")
            if value < 1:             #har ehtimolga qarshi - son kiritishi mumkin foydalanuvchi
                raise serializers.ValidationError("Quantity must be at least 1>")

            return value

        except ObjectDoesNotExist:  #qandaydir xatolik ketsa mahsulot mavjud emas deydi
            raise serializers.ValidationError("Product does not exist")

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        product = order.product
        product.stock -= order.quantity  #productni stokidan miqdorni olib tashlab soxranit qilamiz
        product.save()
        self.send_confirmation_email(order)
        return order

    def send_confirmation_email(self, order):
        print(f"Sent confirmation email for Order {order.id}")





