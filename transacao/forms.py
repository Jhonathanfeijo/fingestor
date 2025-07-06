from django import forms
from .models import Transacao

ISO_DATE = "%Y-%m-%d"

class TransacaoForm(forms.ModelForm):
    
    data = forms.DateField(
        input_formats=[ISO_DATE],
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "block w-full rounded-lg bg-slate-800/60 border border-slate-600/50 "
                         "px-3 py-2 text-white placeholder-gray-400 focus:ring-2 outline-none"
            },
            format=ISO_DATE,
        ),
        label="Data",
        required=True,
    )

    class Meta:
        model = Transacao
        fields = ["tipo_transacao", "valor", "descricao", "categoria", 'data']
        labels = {
            "tipo_transacao": "Tipo",
            "valor": "Valor (R$)",
            "descricao": "Descrição",
            "categoria": "Categoria",
            'data':'Data'
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.data:
            self.fields["data"].initial = self.instance.data.strftime(ISO_DATE)