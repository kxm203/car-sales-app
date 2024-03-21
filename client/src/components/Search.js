import React from "react";

function Search({ mustangs, onChange, value = "" }) {
  const handleInputChange = (event) => {
    const { value } = event.target;
    onChange(value);
  };

  const filteredMustangs = mustangs.filter((mustang) =>
    mustang.model.toLowerCase().includes(value.toLowerCase())
  );

  return (
    <div className="searchbar">
      <label htmlFor="search">Search Mustangs:</label>
      <input
        type="text"
        id="search"
        placeholder="Type model name to search..."
        value={value}
        onChange={handleInputChange}
      />

      {value && (
        <ul>
          {filteredMustangs.map((mustang) => (
            <li key={mustang.model}>
              {mustang.model} {mustang.year} {mustang.color}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Search;
