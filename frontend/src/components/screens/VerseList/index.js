import React, { useState } from "react";
import { useParams } from "react-router-dom";
import { Link } from "react-router-dom";
const stub_verseList = [
  { name: "verse1", number: 1 },
  { name: "verse2", number: 2 }
];
const VerseList = () => {
  let { verses } = useParams();
  const [verseList, setverseList] = useState(stub_verseList);

  return (
    <div className="Page">
      <div className="VerseList">
        {verseList.map(verse => {
          return (
            <Link
              key={verse.number}
              className="VerseListItem"
              to={`/${verses}/${verse.number}`}
            >
              {verse.number}: {verse.name}
            </Link>
          );
        })}
      </div>
    </div>
  );
};

export default VerseList;
