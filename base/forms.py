from django import forms
from pathlib import Path


class CVUploadForm(forms.Form):
    
    cv = forms.FileField(
        label="Upload your CV",
        widget=forms.ClearableFileInput(
            attrs={"accept": ".pdf,.docx"}
        )
    )

    job_description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 6,
                "placeholder": "Paste the target job description..."
            }
        )
    )

    def clean_cv(self):
        cv = self.cleaned_data["cv"]

        extension = Path(cv.name).suffix.lower()

        if extension not in [".pdf", ".docx"]:
            raise forms.ValidationError(
                "Only PDF and DOCX files are supported."
            )

        if cv.size > 5 * 1024 * 1024:
            raise forms.ValidationError(
                "Maximum file size is 5 MB."
            )

        return cv