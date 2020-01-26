import React, { useState } from "react";
import { Link } from "react-router-dom";
const stub_surahList = [
  { name: "The opening", number: 1 },
  { name: "The calf", number: 2 }
];
const SurahList = () => {
  const [surahList, setSurahList] = useState(stub_surahList);

  return (
    <div className="Page">
      <div className="SurahList">
        {surahList.map(surah => {
          return (
            <Link
              className="SurahListItem"
              key={surah.number}
              to={`/${surah.number}`}
            >
              {surah.number}: {surah.name}
            </Link>
          );
        })}
      </div>
    </div>
  );
};

export default SurahList;
