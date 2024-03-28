import React, { useState } from "react";

function NewMustangForm({ addMustang }) {
  //const [model, setModel] = useState("");
  const [year, setYear] = useState("");
  const [color, setColor] = useState("");
  const [price, setPrice] = useState("");
  const [imageUrl, setImageUrl] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    addMustang({ year, color, price, imageUrl });
    //setModel("");
    setYear("");
    setColor("");
    setPrice("");
    setImageUrl("");
  };

  return (
     <form onSubmit={handleSubmit}>
      {/* <label htmlFor="model">Model:</label>
      <input
      type="text"
      id="model"
      value={model}
      onChange={(event) => setModel(event.target.value)}
       /> */}

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
      
      <label htmlFor="imageUrl">Image URL:</label>
      <input
        type="text"
        id="imageUrl"
        value={imageUrl}
        onChange={(event) => setImageUrl(event.target.value)}
      />
      
      
      <button type="submit">Submit</button>

      
    </form>
  );
}

export default NewMustangForm;
