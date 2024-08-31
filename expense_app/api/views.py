from rest_framework import generics
from .serializers import expenseSerializer
from expense_app.models import expense
from rest_framework.permissions import IsAuthenticated
from .permissions import IsExpenseOwner

class expenseCreate(generics.CreateAPIView):
    queryset = expense.objects.all()
    serializer_class = expenseSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
    
class expenseList(generics.ListAPIView):
    serializer_class = expenseSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return expense.objects.filter(user=self.request.user)
    
class expenseDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = expense.objects.all()
    serializer_class = expenseSerializer
    permission_classes = [IsExpenseOwner]
    
    def perform_update(self, serializer):
        user = self.request.user
        
        recurring = serializer.validated_data.get('recurring', False)
        if not recurring:
            serializer.validated_data['recurring_interval'] = None
        serializer.save(user=user)

# class expenseAnalysis(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         user_expenses = expense.objects.filter(user=request.user).values()
#         df = pd.DataFrame(user_expenses)

#         # Debug: Print the DataFrame to check its contents
#         print(df.head())

#         if df.empty:
#             return JsonResponse({'error': 'No data available'}, status=404)

#         # Ensure the date column is in datetime format
#         df['date'] = pd.to_datetime(df['date'], errors='coerce')

#         # Convert amount column to numeric
#         df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

#         # Debug: Print the DataFrame after conversion
#         print(df.head())

#         # Check if `amount` and `date` columns are numeric and datetime respectively
#         if df['amount'].dtype not in ['int64', 'float64'] or df['date'].isna().all():
#             return JsonResponse({'error': 'Invalid data format'}, status=400)

#         # Calculate summaries
#         category_summary = df.groupby('category')['amount'].sum()
#         monthly_summary = df.groupby(df['date'].dt.to_period('M'))['amount'].sum()

#         # Convert Period index to string format
#         monthly_summary.index = monthly_summary.index.astype(str)

#         def plot_to_base64(plt):
#             buf = io.BytesIO()
#             plt.savefig(buf, format='png')
#             buf.seek(0)
#             return base64.b64encode(buf.read()).decode('utf-8')

#         # Plot category summary
#         fig1, ax1 = plt.subplots()
#         if not category_summary.empty:
#             category_summary.plot(kind='bar', ax=ax1)
#             ax1.set_title('Expenses by Category')
#             ax1.set_xlabel('Category')
#             ax1.set_ylabel('Total Amount')
#             category_plot = plot_to_base64(plt)
#         else:
#             category_plot = None
#         plt.close(fig1)

#         # Plot monthly summary
#         fig2, ax2 = plt.subplots()
#         if not monthly_summary.empty:
#             monthly_summary.plot(kind='line', ax=ax2)
#             ax2.set_title('Monthly Expenses')
#             ax2.set_xlabel('Month')
#             ax2.set_ylabel('Total Amount')
#             monthly_plot = plot_to_base64(plt)
#         else:
#             monthly_plot = None
#         plt.close(fig2)

#         response_data = {
#             'category_summary': category_summary.to_dict(),
#             'monthly_summary': monthly_summary.to_dict(),
#             'category_plot': category_plot,
#             'monthly_plot': monthly_plot
#         }

#         return JsonResponse(response_data)