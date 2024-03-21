import React from "react";
import MustangCard from "./MustangCard";

function MustangList({ mustangs, toggleStockStatus }) {
  return (
    <ul className="mustangs">
      {mustangs.map((mustang) => (
        <MustangCard key={mustang.id} mustang={mustang} year={mustang.year} color={mustang.color} mileage={mustang.miles} price={mustang.price} toggleStockStatus= {toggleStockStatus}  />
      ))}
    </ul>
  );
}


export default MustangList;
