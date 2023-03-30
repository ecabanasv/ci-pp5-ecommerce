from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """Default app config for products"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
