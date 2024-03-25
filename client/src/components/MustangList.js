import React from "react";
import MustangCard from "./MustangCard";

function MustangList({ mustangs }) {
  return (
    <ul className="mustangs">
      {mustangs.map((mustang) => (
        <MustangCard key={mustang.id} mustang={mustang} />
      ))}
    </ul>
  );
}

export default MustangList;