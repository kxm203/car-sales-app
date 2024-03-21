import React, { useState } from "react";

function CarCard({ car }) {
    const [isInStock, setIsInStock] = useState(true);

    const toggleStockStatus = () => {
        setIsInStock(!isInStock);
    };

    return (
        <li className="card" data-testid="car-item">
            <img src={car.image} alt={car.year} />
            <h4>{car.year}, {car.color}</h4>
            <p>Price: ${car.price}</p>
            {isInStock ? (
                <button className="primary" onClick={toggleStockStatus}>In Stock</button>
            ) : (
                <button onClick={toggleStockStatus}>Out of Stock</button>
            )}
        </li>
    );
}

export default CarCard;