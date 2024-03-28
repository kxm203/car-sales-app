import React, { useState } from "react";

function Search({ onChange, onSubmit }) {
  const [searchTerm, setSearchTerm] = useState("");

  const handleInputChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    onSubmit(searchTerm);
    console.log("Searching...");
  };

  return (
    <div className="searchbar">
      <form onSubmit={handleSubmit}>
        <label htmlFor="search">Search Mustangs:</label>
        <input
          type="text"
          id="search"
          placeholder="Type a Year to search..."
          value={searchTerm}
          onChange={handleInputChange}
        />
        <button type="submit">Search</button>
      </form>
    </div>
  );
}

export default Search;
