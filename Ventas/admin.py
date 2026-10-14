from django.contrib import admin
from Ventas.models import Cliente, Pedido

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'email', 'fecha_nacimiento', 'numero_telefono')
    list_filter = ('fecha_nacimiento', 'numero_telefono')
    search_fields = ('rut', 'nombre', 'email')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('ID', 'cliente', 'fecha', 'total_formateado')
    list_filter = ('fecha', )
    search_fields = ('ID', 'cliente_nombre', 'fecha', 'total_formateado')

    def total_formateado(self, obj):
        return f"${obj.total:,}".replace(',', '.')