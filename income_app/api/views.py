from .serializers import incomeSerializers
from rest_framework import generics
from income_app.models import income
from rest_framework.permissions import IsAuthenticated
from .permissions import IsIncomeOwner

class incomeCreate(generics.CreateAPIView):
    queryset = income.objects.all()
    serializer_class = incomeSerializers
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        
class incomeList(generics.ListAPIView):
    serializer_class = incomeSerializers
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return income.objects.filter(user=self.request.user)
    
class incomeDetails(generics.RetrieveUpdateAPIView):
    serializer_class = incomeSerializers
    permission_classes = [IsIncomeOwner]
    queryset = income.objects.all()
    
    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(user=user)