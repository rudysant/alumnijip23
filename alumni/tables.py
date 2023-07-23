import django_tables2 as tables
from .models import TestData, Profile

class PaginatedTable(tables.Table):
    class Meta:
        model = Profile
        template_name = "paginated.html"  # Use your preferred template

    # Add any additional columns or customization as needed
