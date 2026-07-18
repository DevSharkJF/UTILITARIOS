import whisper
from tqdm import tqdm
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
VIDEO_PATH = str(SCRIPT_DIR / "arquivo.extensao")
OUTPUT_TXT = str(SCRIPT_DIR / "transcricao.txt")
MODEL_NAME = "base"

model = whisper.load_model(MODEL_NAME)

print(f"Transcrevendo {VIDEO_PATH} com o modelo {MODEL_NAME}... \n")

result = model.transcribe(
    VIDEO_PATH, 
    verbose=True,
    fp16=False, 
    word_timestamps=False
)

print("\n [TRANSCRIÇÃO COMPLETA]\n")
print(result["text"])