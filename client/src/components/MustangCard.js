import React, { useState } from "react";

function MustangCard({ mustang, toggleStockStatus }) {
  const [isInStock, setIsInStock] = useState(true);

  const handleClick = () => {
    setIsInStock(!isInStock);
    toggleStockStatus(mustang.id);
  };

  return (
    <li className="card" data-testid="mustang-item">
      <img src={mustang.image} alt={mustang.year} />
      <h4>{mustang.year}, {mustang.color}</h4>
      <p>Price: ${mustang.price}</p>
      {isInStock ? (
        <button className="primary" onClick={handleClick}>In Stock</button>
      ) : (
        <button onClick={handleClick}>Out of Stock</button>
      )}
    </li>
  );
}

export default MustangCard;