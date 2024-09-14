from django.contrib import admin
from .models import ashuvarity, AshuCertificate, AshuReview, Store
# Register your models here.
class AshuReviewInline(admin.TabularInline):
    model = AshuReview
    extra = 2

class AshuVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [AshuReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('ashu_varieties',)

class AshuCertificateAdmin(admin.ModelAdmin):
    list_display = ('ashu', 'certificate_number')

admin.site.register(ashuvarity, AshuVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(AshuCertificate, AshuCertificateAdmin)
