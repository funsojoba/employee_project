from .views import EmployeeView

urlpatterns = [
    path('', EmployeeView.as_view(), name='employee'),
]
