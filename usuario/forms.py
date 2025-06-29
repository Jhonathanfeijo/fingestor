from django import forms
from .models import Usuario

TAILWIND_INPUT_CLASSES = (
    "w-full p-2 rounded bg-gray-700 text-white "
    "focus:outline-none focus:ring-2 focus:ring-blue-500"
)

class FormRegistroUsuario(forms.ModelForm):
    senha = forms.CharField(
        widget=forms.PasswordInput()
    )
    
    confirme_senha = forms.CharField(
        widget=forms.PasswordInput()
    )
    
    meta = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={"step": "0.01"}),
    )

    def __init__(self, *args, **kwargs):
        super(FormRegistroUsuario, self).__init__(*args, **kwargs)

        # Aplica as classes Tailwind em TODOS os campos
        for field in self.fields.values():
            # Mantém classes que o Django já colocou (por ex. 'form-control')
            css_atual = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"{css_atual} {TAILWIND_INPUT_CLASSES}".strip()

    def clean(self):
        cleaned_data = super(FormRegistroUsuario, self).clean()
        senha = cleaned_data.get('senha')
        confirme_senha = cleaned_data.get('confirme_senha')
        
        if senha != confirme_senha:
            raise forms.ValidationError("As senhas não conferem")

    class Meta:
        model = Usuario
        fields = ["nome", "email", "meta", "senha"]

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "email", "meta"]      # ajuste se tiver mais campos
        labels = {
            "nome":  "Nome",
            "email": "E‑mail",
            "meta":  "Meta (R$)",
        }
        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class": (
                        "block w-full rounded-md bg-gray-700 border border-gray-600 "
                        "px-3 py-2 text-white placeholder-gray-400 "
                        "focus:ring-2 focus:ring-green-500 outline-none"
                    )
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": (
                        "block w-full rounded-md bg-gray-700 border border-gray-600 "
                        "px-3 py-2 text-white placeholder-gray-400 "
                        "focus:ring-2 focus:ring-green-500 outline-none"
                    )
                }
            ),
            "meta": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "min": "0",
                    "class": (
                        "block w-full rounded-md bg-gray-700 border border-gray-600 "
                        "px-3 py-2 text-white placeholder-gray-400 "
                        "focus:ring-2 focus:ring-green-500 outline-none"
                    ),
                }
            ),
        }

    # evita que o usuário salve um e‑mail já usado por outra conta
    def clean_email(self):
        email = self.cleaned_data["email"]
        qs = Usuario.objects.filter(email=email).exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Este e‑mail já está em uso.")
        return email
        