import React from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import styles from "./Map.module.css";
import Checkbox from "./Checkbox";
import { useEffect, useState } from "react";
import axios from "axios";

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
        zoom={25}
        scrollWheelZoom={false}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <Marker position={[places.Latitude, places.Longitude]}>
          <Popup>
            <Checkbox title={places.Name} />
          </Popup>
        </Marker>
      </MapContainer>
    </div>
  );
};
