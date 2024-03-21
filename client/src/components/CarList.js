import React from "react";
import CarCard from "./CarCard";

function CarList({ cars, toggleStockStatus }) {
  return (
    <ul className="cars">
      {cars.map((car) => (
        <CarCard key={car.id} car={car} year={car.year} color={car.color} mileage={car.miles} price={car.price} toggleStockStatus= {toggleStockStatus}  />
      ))}
    </ul>
  );
}


export default CarList;
