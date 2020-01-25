from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root_page():
    return {"quran": "translation"}

@app.get("/get-translator/{surah}/{ayah}/{word_index}")
def get_translation(surah, ayah, word_index):
    return {"surah": surah, "ayah": ayah, "word": word_index}


@app.get("/retranslate/{surah}/{ayah}/{word_index}")
def retranslate(surah, ayah, word_index):
    return dict(Text="New Translation")

