import React from "react";

function Search({onChange}) {
const handleInputChnage = (event) => {
  const { value } = event.target;
  onChange(value);
  console.log("Searching...")
}

  return (
    <div className="searchbar">
      <label htmlFor="search">Search Mustangs:</label>
      <input
        type="text"
        id="search"
        placeholder="Type a Year to search..."
        onChange= {handleInputChnage}
      />
    </div>
  );
}

export default Search;
