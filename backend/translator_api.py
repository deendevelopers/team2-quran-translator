from fastapi import FastAPI
from data_processing.xml_to_dataframe import gather_translations_df

app = FastAPI()

@app.get("/")
def root_page():
    return {"quran": "translation"}

@app.get("/get-translator/{surah}/{verse_no}/{word_index}")
def get_translation(surah, verse_no, word_index):
    data = gather_translations_df()["en_sahih"].loc[surah, verse_no]
    return dict(Translation=data)


@app.get("/retranslate/{surah}/{verse_no}/{word_index}")
def retranslate(surah, verse_no, word_index):
    return dict(Text="New Translation")

