import React, { useState } from "react";
const stub_wordList = {
  translation: "Praise belongs to God, Lord*  of the Worlds",
  words: [
    {
      surah: 1,
      aayah: 1,
      word: 0,
      name: "ٱلْحَمْدُ",
      translation: ["All praise", "All thanks"] //if empty
    },
    {
      surah: 1,
      aayah: 1,
      word: 1,
      name: "لِلَّهِ",
      translation: [] //if empty
    },
    {
      surah: 1,
      aayah: 1,
      word: 2,
      name: "رَبِّ",
      translation: [] //if empty
    },
    {
      surah: 1,
      aayah: 1,
      word: 3,
      name: "ٱلْعَٰلَمِينَ",
      translation: ["the worlds", "those with intelligence"] //if empty
    }
  ]
};
const WordPage = () => {
  const [chosenWord, setChosenWord] = useState(undefined);
  const [wordList, setWordList] = useState(stub_wordList);
  const [modalPosition, setModalPosition] = useState({});

  const handleWordClick = (e, word) => {
    setChosenWord(word);
    console.log(e.offsetX);
    console.log(e.offsetY);
    setModalPosition({ top: e.clientY + 30, left: e.clientX - 30 });
    // console.log(modalPosition);
  };

  return (
    <div className="Page">
      <div className="ArabicVerse">
        {wordList.words.map(word => {
          if (word.translation.length !== 0) {
            return (
              <span
                key={word.name}
                className="ArabicWord __highlighted"
                onClick={e => handleWordClick(e, word)}
              >
                {word.name}
              </span>
            );
          }
          return (
            <span key={word.name} className="ArabicWord">
              {word.name + " "}
            </span>
          );
        })}
      </div>
      <p className="EnglishTranslation">{wordList.translation}</p>
      {chosenWord && (
        <div className="TranslationTooltip" style={modalPosition}>
          <p className="HighlightedWord">{chosenWord.name}</p>
          <div className="TranslationOptionsList">
            {chosenWord.translation.map(word => {
              return <button className="TranslationOption">{word}</button>;
            })}
          </div>
        </div>
      )}
    </div>
  );
};

export default WordPage;
