from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import Order, Coupon
from .serializers import OrderSerializer, CouponSerializer

class CheckoutViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    @action(detail=False, methods=['post'])
    def create_session(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save(user=request.user, status='pending')
            
            # Here you would integrate with your payment provider
            # For example, create a payment intent with Stripe
            
            return Response({
                'sessionId': str(order.id),
                'total': float(order.total_amount),
                'currency': 'USD',
                'status': order.status
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def validate_coupon(self, request):
        code = request.data.get('code')
        try:
            coupon = Coupon.objects.get(
                code=code,
                valid_from__lte=timezone.now(),
                valid_until__gte=timezone.now(),
                is_active=True
            )
            return Response({
                'valid': True,
                'discount': coupon.discount_percent
            })
        except Coupon.DoesNotExist:
            return Response({'valid': False}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['post'])
    def shipping_rates(self, request):
        # Mock shipping rates - in production, integrate with shipping providers
        return Response([
            {
                'id': 'standard',
                'carrier': 'Standard Shipping',
                'price': 5.99,
                'estimatedDays': 5
            },
            {
                'id': 'express',
                'carrier': 'Express Shipping',
                'price': 14.99,
                'estimatedDays': 2
            }
        ])