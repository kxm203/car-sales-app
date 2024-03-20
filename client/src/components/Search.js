import React from "react";

function Search({onChange}) {
  const handleInputChange = (event) => {
    const { value } = event.target;
    onChange(value);
    console.log("Searching...");
  }
  return (
    <div className="searchbar">
      <label htmlFor="search">Search Mustangs:</label>
      <input
        type="text"
        id="search"
        placeholder="Type details to search ex. year, color..."
        onChange={handleInputChange}
      />
    </div>
  );
}

export default Search;
