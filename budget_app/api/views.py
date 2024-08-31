from .serializers import budgetSerializer
from rest_framework import generics
from budget_app.models import budget
from rest_framework.permissions import IsAuthenticated
from .permissions import IsBudgetOwner

class budgetCreate(generics.CreateAPIView):
    queryset = budget.objects.all()
    serializer_class = budgetSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        
class budgetList(generics.ListAPIView):
    serializer_class = budgetSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return budget.objects.filter(user=self.request.user)
    
class budgetDetails(generics.RetrieveUpdateAPIView):
    serializer_class = budgetSerializer
    permission_classes = [IsBudgetOwner]
    queryset = budget.objects.all()
    
    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(user=user)