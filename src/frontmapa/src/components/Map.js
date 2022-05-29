import React from "react";
import { MapContainer, TileLayer } from "react-leaflet";
import styles from "./Map.module.css";
import { useEffect, useState } from "react";
import axios from "axios";
import Pin from "./Pin";

export const Map = () => {
  const [isLoading, setIsLoading] = useState(true);
  const [places, setPlaces] = useState([]);

  useEffect(() => {
    setIsLoading(false);
    axios.get("http://localhost:5000/places").then((res) => {
      setPlaces(res.data);
    });
  }, [setIsLoading]);

  if (isLoading) {
    return (
      <section>
        <p>Loading...</p>
      </section>
    );
  }

  return (
    <div className={styles.mapbox}>
      <MapContainer
        center={[41.4275103, 2.1833535]}
        zoom={15}
        scrollWheelZoom={true}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {places.map((place) => (
          <Pin place={place} />
        ))}
      </MapContainer>
    </div>
  );
};
