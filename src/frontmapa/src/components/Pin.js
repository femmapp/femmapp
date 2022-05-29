import { Marker, Popup } from "react-leaflet";
import CheckboxesGroup from "./Checkbox";
import React from "react";

export default function Pin({ place }) {
  console.log(place);
  return (
    <Marker position={[place.Latitude, place.Longitude]}>
      <Popup>
        <CheckboxesGroup title={place.Name} />
      </Popup>
    </Marker>
  );
}
