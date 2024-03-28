import React, { useState, useEffect } from "react";

function MustangCard({ mustang, toggleStockStatus }) {
  const [isInStock, setIsInStock] = useState(true);
  const [price, setPrice] = useState(mustang.price);
  const [bidAmount, setBidAmount] = useState(null);

  useEffect(() => {
    fetchBidAmount();
  }, []);

  const fetchBidAmount = () => {
    fetch(`http://localhost:5555/bids/${mustang.id}`)
      .then((response) => response.json())
      .then((data) => {
        setBidAmount(data.bid_amount);
      })
      .catch((error) => {
        console.error("Error fetching bid amount:", error);
      });
  };

  const handleUpdateBid = () => {
    const newBidAmount = bidAmount + 1000;

    fetch(`http://localhost:5555/bids/${mustang.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ bid_amount: newBidAmount }),
    })
    .then((response) => response.json())
    .then((data) => {
      setBidAmount(data.bid_amount);
    })
    .catch((error) => {
      console.error("Error updating bid amount:", error);
    });
  };

  const handleClick = () => {
    setIsInStock(!isInStock);
    toggleStockStatus(mustang.id);
  };

  return (
    <li className="card" data-testid="mustang-item">
      <img src={mustang.image_url} alt={`${mustang.year} ${mustang.color}`} />
      <h4>{mustang.year}, {mustang.color} </h4>
      <p>Price: ${price}</p>
      <p>Bid: ${bidAmount !== null ? bidAmount : "Loading..."}</p>
      <button onClick={handleUpdateBid}>Update Bid</button>
      {isInStock ? (
        <button className="primary" onClick={handleClick}>In Stock</button>
      ) : (
        <button onClick={handleClick}>Out of Stock</button>
      )}
    </li>
  );
}

export default MustangCard;