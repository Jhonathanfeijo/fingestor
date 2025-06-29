from django import forms
from .models import Transacao


class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ["tipo_transacao", "valor", "descricao", "categoria"]
        labels = {
            "tipo_transacao": "Tipo",
            "valor": "Valor (R$)",
            "descricao": "Descrição",
            "categoria": "Categoria",
        }
        widgets = {
            "tipo_transacao": forms.Select(
                attrs={
                    "class": "block w-full rounded-lg bg-slate-800/60 border border-slate-600/50 "
                    "px-3 py-2 text-white focus:ring-2 outline-none"
                }
            ),
            "valor": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "min": "0",
                    "class": "block w-full rounded-lg bg-slate-800/60 border border-slate-600/50 "
                    "px-3 py-2 text-white placeholder-gray-400 focus:ring-2 outline-none"
                }
            ),
            "descricao": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "block w-full rounded-lg bg-slate-800/60 border border-slate-600/50 "
                    "px-3 py-2 text-white placeholder-gray-400 focus:ring-2 outline-none"
                }
            ),
            "categoria": forms.Select(
                attrs={
                    "class": "block w-full rounded-lg bg-slate-800/60 border border-slate-600/50 "
                    "px-3 py-2 text-white focus:ring-2 outline-none"
                }
            ),
        }
