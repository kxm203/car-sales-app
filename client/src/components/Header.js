import React from "react";
import mustangsImage from "./mustangs.jpg"; // Import your image

function Header() {
  return (
    <header>
      <h1>
        Classic Mustangs
        <img src={mustangsImage} alt="Mustangs" className="logo" /> {/* Replace the emoji with the image */}
      </h1>
    </header>
  );
}

export default Header;
