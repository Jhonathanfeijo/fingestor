from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def calcular_saldo(meta, valor):
    # Garantir que meta e valor são Decimal
    try:
        meta = Decimal(meta)
        valor = Decimal(valor)
    except:
        return ''

    saldo = meta - valor
    return saldo
