from typing import List
import json

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import pandas as pd

with open('data/trans_var.json', 'r') as f:
    trans_json = json.load(f)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df_trans = pd.read_pickle('data/df_translation.pckl')

DEFAULT_TRANS = 'en_sahih'



@app.get("/")
def root_page():
    return {"quran": "translation"}


@app.get('/get-surah-list/')
def get_surah_list():
    return [{"name": s,  "number": i + 1} for i, s in
            enumerate(df_trans['Surah Name'].unique().tolist())]


@app.get("/{surah}")
def get_verses_text(surah: int):
    verses = []
    i = 1
    for index, row in df_trans.loc[surah][['Verse Text', DEFAULT_TRANS]].iterrows():
        verses.append(
            {'text': row['Verse Text'],
             'translation': row[DEFAULT_TRANS],
             'number': i}
        )
        i += 1
    return verses


@app.get("/{surah}/{verse}")
def get_verse(surah: int, verse: int):
    verses = []
    i = 1
    for index, row in df_trans.loc[surah][['Verse Text', DEFAULT_TRANS]].iterrows():
        verses.append(
            {'text': row['Verse Text'],
             'translation': row[DEFAULT_TRANS],
             'number': i}
        )
        i += 1

    r = trans_json['verses'][verse - 1]
    r['translation'] = verses[verse]['translation']
    return r


@app.get("/get-translator/{surah}/{verse_no}/{word_index}")
def get_translation(surah: int, verse_no: int, word_index):
    data = df_trans["en_sahih"].loc[surah, verse_no]
    return dict(Translation=data)


@app.get("/retranslate/{surah}/{verse}/{word_idx}/{trans_option}")
def retranslate(surah: int, verse: int, word_idx: int, trans_option: int):
    new_trans = ''
    verse_json = trans_json['verses'][verse - 1]
    for idx, word_json in enumerate(verse_json['words']):
        print(new_trans)
        print(idx, word_json)
        if idx == word_idx:
            new_trans += word_json['trans_variations'][trans_option]['en_trans']
        else:
            new_trans += word_json['trans_variations'][0]['en_trans']
    return new_trans
