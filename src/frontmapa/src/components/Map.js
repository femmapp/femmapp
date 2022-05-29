import React from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import styles from "./Map.module.css";
import Checkbox from "./Checkbox";

/* import { useEffect, useState } from "react";
import axios from "axios";
import api from "../globalapi"; */

export const Map = () => {
  return (
    <div className={styles.mapbox}>
      <MapContainer
        center={[41.42759, 2.18476]}
        zoom={25}
        scrollWheelZoom={true}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <Marker position={[41.42759, 2.18476]}>
          <Popup>
            <Checkbox />
          </Popup>
        </Marker>
      </MapContainer>
    </div>
  );
};
