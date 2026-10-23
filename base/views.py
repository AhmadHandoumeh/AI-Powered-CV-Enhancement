from django.shortcuts import render
from .models import Post
from pathlib import Path
from django.shortcuts import render
from .forms import CVUploadForm
from .pdf_extractor import extract_pdf_text
from .docx_extractor import extract_docx_text
from openai import OpenAIError
from .analyzer import analyze_cv




# Create your views here.

def upload_cv(request):
  
  if request.method == "POST":

    form = CVUploadForm(request.POST, request.FILES)

    if form.is_valid():
      
      cv = form.cleaned_data["cv"]
      job_description = form.cleaned_data["job_description"]


      extension = Path(cv.name).suffix.lower()

      try:
          if extension == ".pdf":
              extracted_text = extract_pdf_text(cv)
          else:
              extracted_text = extract_docx_text(cv)

      except Exception:
          form.add_error(
              "cv",
              "Unable to read this file. Please upload a valid PDF or DOCX."
          )
      else:
          if not extracted_text:
              form.add_error(
                  "cv",
                  "No readable text was found in this CV."
              )



          else:
            try:
                analysis = analyze_cv(
                    extracted_text,
                    job_description
                )


            except (OpenAIError, ValueError) as e:
                form.add_error(
                    None,
                    "AI analysis failed. Please try again."
                )


            else:
                
                return render(
                    request,
                    "base/home.html",
                    {
                        "page": "display",
                        "analysis": analysis,
                        "filename": cv.name,
                        "job_description": job_description,
                        "extracted_text": extracted_text
                    }
                )
            



  else:
      form = CVUploadForm()

  return render(
      request,
      "base/home.html",
      {
        "page": "",
        "form": form
       }
  )


