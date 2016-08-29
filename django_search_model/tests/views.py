from django_search_model.list import SearchableListView
from .models import Device, Provider, Brand

class ListDevicePaginate(SearchableListView):
    model = Device
    template_name = "tests/list.html"
    paginate_by = 10

class ListDeviceSearchablePaginate(SearchableListView):
    model = Device
    template_name = "tests/list.html"
    paginate_by = 10
    searchable_fields = ["inventory_number", "model_device", "model_device__brand__provider",
    "model_device__brand__name"]

class ListDeviceReverseRelationFail(SearchableListView):
    model = Provider
    template_name = "tests/list_reverse.html"
    paginate_by = 2
    searchable_fields = ["brand", "brand__modeldevice__device"]

class ListDeviceReverseRelation(SearchableListView):
    model = Brand
    template_name = "tests/list_reverse_brand.html"
    paginate_by = 2
    searchable_fields = ["modeldevice"]