from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import AsyncGroq
import os

# =====================================================
# ENV & CLIENT SETUP
# =====================================================
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("FATAL: GROQ_API_KEY tidak ditemukan di file .env")

groq_client = AsyncGroq(api_key=GROQ_API_KEY)

# =====================================================
# FASTAPI APP
# =====================================================
app = FastAPI(
    title="kating.AI Backend",
    description="Backend API untuk merapikan bahasa skripsi dan teks akademik",
    version="1.0.0",
)

# =====================================================
# CORS (WAJIB UNTUK FRONTEND)
# =====================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ganti dengan domain Vercel saat production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================
# DATA MODELS
# =====================================================
class HumanizeRequest(BaseModel):
    text: str

class HumanizeResponse(BaseModel):
    result: str

# =====================================================
# UTILITIES
# =====================================================
def count_words(text: str) -> int:
    return len([w for w in text.split() if w.strip()])


def build_standard_prompt(user_text: str):
    system_prompt = (
        "Kamu adalah Kating.AI, penulis akademik Bahasa Indonesia yang berpengalaman dan manusiawi. "
        "Tugasmu adalah menulis ulang teks menjadi bahasa akademik baku sesuai PUEBI, "
        "dengan gaya yang alami dan tidak mekanis.\n\n"

        "PRINSIP UTAMA:\n"
        "- Makna teks harus dipertahankan sepenuhnya.\n"
        "- Hasil tulisan harus terdengar seperti ditulis manusia, bukan hasil generasi otomatis.\n\n"

        "PEDOMAN GAYA PENULISAN (WAJIB):\n"
        "1. Variasikan panjang dan kompleksitas kalimat secara alami. "
        "Gunakan kombinasi kalimat pendek yang tegas dan kalimat panjang dengan anak kalimat bertingkat. "
        "Hindari ritme kalimat yang seragam.\n\n"

        "2. Jangan selalu memulai kalimat dengan subjek. "
        "Gunakan inversi, keterangan awal, atau klausa pengantar di tengah kalimat bila sesuai konteks.\n\n"

        "3. Hindari diksi akademik yang terlalu generik atau sering muncul dalam tulisan otomatis, "
        "seperti: 'signifikan', 'merupakan', 'hal ini', 'dapat disimpulkan', 'oleh karena itu'. "
        "Gunakan sinonim yang lebih kontekstual dan jarang diulang, namun tetap baku dan tepat makna.\n\n"

        "4. Variasikan pola hubungan sebab–akibat. "
        "Jangan menggunakan struktur langsung 'A menyebabkan B'. "
        "Gunakan formulasi implisit, reflektif, atau deskriptif sesuai konteks akademik.\n\n"

        "5. Jaga alur tetap logis, tetapi jangan terlalu simetris atau terlalu rapi. "
        "Biarkan transisi antarkalimat terasa alami seperti tulisan mahasiswa tingkat akhir "
        "yang matang secara intelektual.\n\n"

        "6. Jangan menambahkan opini baru, data baru, atau kesimpulan yang tidak ada di teks asli.\n\n"

        "ATURAN OUTPUT:\n"
        "- Langsung tampilkan hasil parafrase.\n"
        "- Jangan menambahkan penjelasan, pembuka, atau catatan apa pun."
    )


    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_text},
    ]

# =====================================================
# API ENDPOINT
# =====================================================
@app.post("/api/humanize", response_model=HumanizeResponse)
async def humanize_text(payload: HumanizeRequest):
    text = payload.text.strip()

    if not text:
        raise HTTPException(
            status_code=400,
            detail="Teks tidak boleh kosong."
        )

    # =========================
    # WORD LIMIT LOGIC
    # =========================
    MIN_WORDS = 50
    MAX_WORDS = 300

    word_count = count_words(text)

    if word_count < MIN_WORDS:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Teks terlalu pendek untuk diproses. "
                f"Minimal {MIN_WORDS} kata diperlukan agar hasil humanisasi optimal. "
                f"Teks kamu saat ini: {word_count} kata."
            ),
        )

    if word_count > MAX_WORDS:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Versi gratis maksimal {MAX_WORDS} kata. "
                f"Teks kamu berjumlah {word_count} kata."
            ),
        )

    messages = build_standard_prompt(text)

    try:
        completion = await groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.85,
            top_p=0.9,
            max_tokens=1024,
        )

        result_text = completion.choices[0].message.content.strip()

        if not result_text:
            raise HTTPException(
                status_code=500,
                detail="Gagal menghasilkan teks. Silakan coba ulang."
            )

        return {"result": result_text}

    except HTTPException:
        raise

    except Exception as e:
        print(f"[ERROR] {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Server kating.AI sedang bermasalah. Silakan coba lagi nanti."
        )


# =====================================================
# HEALTH CHECK
# =====================================================
@app.get("/")
def health_check():
    return {
        "status": "online",
        "service": "kating.AI backend",
        "version": "1.0.0",
    }
