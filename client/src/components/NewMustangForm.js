import React, { useState } from "react";

function NewMustangForm({ addMustang }) {
  const [imageUrl, setImageUrl] = useState("");
  const [year, setYear] = useState("");
  const [color, setColor] = useState("");
  const [price, setPrice] = useState("");


  const handleSubmit = (event) => {
    event.preventDefault();
    addMustang({ imageUrl, year, color, price });
    setImageUrl("");
    setYear("");
    setColor("");
    setPrice("");
    setImageUrl("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="imageUrl">Image URL:</label>
      <input
        type="text"
        id="imageUrl"
        value={imageUrl}
        onChange={(event) => setImageUrl(event.target.value)}
      />

      <label htmlFor="year">Year:</label>
      <input
        type="number"
        id="year"
        value={year}
        onChange={(event) => setYear(event.target.value)}
      />

      <label htmlFor="color">Color:</label>
      <input
        type="text"
        id="color"
        value={color}
        onChange={(event) => setColor(event.target.value)}
      />

      <label htmlFor="price">Price:</label>
      <input
        type="number"
        id="price"
        value={price}
        onChange={(event) => setPrice(event.target.value)}
      />

      <button type="submit">Submit</button>


    </form>
  );
}

export default NewMustangForm;
