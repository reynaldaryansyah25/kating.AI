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
        "Kamu adalah 'Kating.AI', editor akademik profesional. Tugasmu memperbaiki teks user menjadi kalimat skripsi/jurnal yang baku, padat, dan efektif.\n\n"
        
        "ATURAN EDITING:\n"
        "1. [Diksi Akademik]: Ganti kata sehari-hari dengan istilah ilmiah (cth: 'banget' -> 'secara signifikan', 'dilihat' -> 'diamati').\n"
        "2. [Kalimat Efektif]: Hindari pemborosan kata (pleonasme). Jangan bertele-tele. Buat kalimat yang 'punchy' dan langsung ke inti.\n"
        "3. [Struktur Pasif]: Gunakan struktur pasif (di-) untuk menekankan objek penelitian, bukan pelakunya.\n"
        "4. [Natural]: Hasil harus mengalir luwes. HINDARI frasa kaku seperti 'dalam hal ini', 'adapun', atau menyebut 'variabel tersebut' secara eksplisit jika tidak perlu.\n"
        "5. [Substansi]: Pertahankan makna asli 100%, jangan menambah asumsi baru.\n\n"
        
        "Langsung berikan hasil revisi terbaikmu."
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
        raise HTTPException(status_code=400, detail="Teks tidak boleh kosong")

    word_count = count_words(text)
    if word_count > 150:
        raise HTTPException(
            status_code=400,
            detail=f"Versi gratis maksimal 150 kata. Teks kamu berjumlah {word_count} kata.",
        )

    messages = build_standard_prompt(text)

    try:
        completion = await groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.4,
            max_tokens=1024,
        )

        result_text = completion.choices[0].message.content.strip()

        if not result_text:
            raise HTTPException(
                status_code=500,
                detail="Gagal menghasilkan teks. Silakan coba ulang.",
            )

        return {"result": result_text}

    except HTTPException:
        raise

    except Exception as e:
        print(f"[ERROR] {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Server kating.AI sedang bermasalah. Silakan coba lagi nanti.",
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
