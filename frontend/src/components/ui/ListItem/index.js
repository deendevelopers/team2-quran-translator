import React from "react";

const List = ({ onClick, number, name }) => (
  <li onClick={onClick}>
    <h3>
      {number}: {name}
    </h3>
  </li>
);

export default List;
