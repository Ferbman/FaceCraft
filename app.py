from flask import Flask, request, render_template
import subprocess
import uuid
import os

app = Flask(__name__)

OUTPUT_DIR = "static/outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    image_filename = None
    error_message = None
    # Kullanıcının girdiği metni tutmak için bir değişken ekliyoruz
    description_text = ""

    if request.method == "POST":
        # Formdan gelen metni alıp hem text değişkenine hem de
        # sayfaya geri göndereceğimiz description_text'e atıyoruz.
        text = request.form.get("description", "").strip()
        description_text = text

        if not text:
            error_message = "Lütfen bir açıklama girin."
        else:
            output_file = f"{uuid.uuid4().hex}.png"
            output_path = os.path.join(OUTPUT_DIR, output_file)

            try:
                # modified_resim.py'yi subprocess ile çağır
                result = subprocess.run(
                    ["python", "modified_resim.py", text, output_path],
                    capture_output=True,
                    text=True,
                    timeout=None # Gerekirse bir zaman aşımı süresi belirleyebilirsiniz, örn: timeout=120 (120 saniye)
                )

                if result.returncode == 0:
                    image_filename = output_file
                else:
                    error_message = f"Hata oluştu:<br><pre>{result.stderr}</pre>"

            except subprocess.TimeoutExpired:
                error_message = "İşlem zaman aşımına uğradı."
            except FileNotFoundError:
                error_message = "Hata: 'python' komutu bulunamadı veya 'modified_resim.py' dosyası mevcut değil."
            except Exception as e:
                error_message = f"Beklenmedik bir hata oluştu: {e}"

    # render_template fonksiyonuna description_text değişkenini ekliyoruz.
    # HTML tarafında 'error' değişkenini kullandığımız için error=error_message şeklinde eşleştirme yapıyoruz.
    return render_template("index.html", 
                           image_filename=image_filename, 
                           error=error_message, 
                           description_text=description_text)

if __name__ == "__main__":
    app.run(debug=True)