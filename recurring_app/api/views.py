from rest_framework import generics
from .serializers import recurringSerializer
from recurring_app.models import recurring
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permission import IsRecurringOwner

class recurringCreate(generics.CreateAPIView):
    queryset = recurring.objects.all()
    serializer_class = recurringSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        