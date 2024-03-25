import React from "react" 
import {NavLink} from "react-router-dom"

function Welcome() {
    return (
      <div className="welcome-container">
        <h1 className="welcome-heading">BID YOUR MUSTANG</h1>
        <img
          className="car-image"
          src="https://www.pngmart.com/files/16/Cheese-Burger-PNG-Photos.png"
          alt="CLassic Mustang"
        />
        <NavLink className="get-bidding-link" to="/App">
          *~-CLICK ME TO GET BIDDING!-~*
        </NavLink>
      </div>
    );
  }

export default Welcome