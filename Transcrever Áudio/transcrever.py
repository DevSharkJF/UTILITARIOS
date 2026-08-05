import whisper
from tqdm import tqdm
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
VIDEO_PATH = str(SCRIPT_DIR / "arquivo.extensao")
OUTPUT_TXT = str(SCRIPT_DIR / "transcricao.txt")
MODEL_NAME = "base"

model = whisper.load_model(MODEL_NAME)

print(
    "\n"
    "------------------------------------------------------------------------ INICIANDO A TRANSCRIÇÃO ------------------------------------------------------------------------"
)
print(
    f"📝 Transcrevendo {VIDEO_PATH}"
    f"\n🤖 Utilizando o Modelo: {MODEL_NAME}"
)

print(
    "\n"
    "------------------------------------------------------------------------ TRANSCRIÇÃO POR PARTES ------------------------------------------------------------------------"
)
result = model.transcribe(
    VIDEO_PATH, 
    verbose=True,
    fp16=False, 
    word_timestamps=False
)
print(
    "✅ TRANSCRIÇÃO POR PARTES CONCLUÍDA ✅"
)

# Transcrição Completa pelo Terminal
print(
    "\n" 
    "------------------------------------------------------------------------ TRANSCRIÇÃO COMPLETA ------------------------------------------------------------------------"
)
print(result["text"], "\n")

# Transcrição Completa por partes e salvando em um arquivo TXT
with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
    for seg in tqdm (result["segments"], desc="Salvando transcrição"):
        start = seg["start"]
        end = seg["end"]
        text = seg["text"].strip()
        f.write(f"[{start:.2f} --> {end:.2f}] {text}\n")

# print(f"\n[INFO] Transcrição salva em '{OUTPUT_TXT}'\n")
print(
    f"💾 A TRANSCRIÇÃO FOI SALVA NO CAMINHO: '{OUTPUT_TXT}'"
    "\n"
)

# Transcrição Completa salvando em um arquivo TXT o texto completo
with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
    f.write(result["text"])
print(
    f"💾 A TRANSCRIÇÃO FOI SALVA NO CAMINHO: '{OUTPUT_TXT}'"
    "\n"
)