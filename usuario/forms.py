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
        fields = ["nome", "email", "meta", "senha",'confirme_senha']
