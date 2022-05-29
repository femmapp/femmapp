import * as React from "react";
import Box from "@mui/material/Box";
import FormLabel from "@mui/material/FormLabel";
import FormControl from "@mui/material/FormControl";
import FormGroup from "@mui/material/FormGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
//import FormHelperText from "@mui/material/FormHelperText";
import Checkbox from "@mui/material/Checkbox";

export default function CheckboxesGroup() {
  const [state, setState] = React.useState({
    cambiador: true,
    zona_lactancia: false,
    espacio_infantil: true,
    canguraje: false,
    accesible_ruedas: true,
    baño_mixto: true,
    baño_lavamanos: true,
    LGTBQ_friendy: true,
    ginecologia: false,
    psicologia: false,
    red_flag: false,
  });

  const handleChange = (event) => {
    setState({
      ...state,
      [event.target.name]: event.target.checked,
    });
  };

  const {
    cambiador,
    zona_lactancia,
    espacio_infantil,
    canguraje,
    accesible_ruedas,
    baño_mixto,
  } = state;

  return (
    <Box sx={{ display: "flex" }}>
      <FormControl sx={{ m: 3 }} component="fieldset" variant="standard">
        <FormLabel component="legend">Canodrom</FormLabel>
        <FormGroup>
          <FormControlLabel
            control={
              <Checkbox
                checked={cambiador}
                onChange={handleChange}
                name="cambiador"
              />
            }
            label="Cambiador"
          />
          <FormControlLabel
            control={
              <Checkbox
                checked={zona_lactancia}
                onChange={handleChange}
                name="zona_lactancia"
              />
            }
            label="Zona de lactancia"
          />
          <FormControlLabel
            control={
              <Checkbox
                checked={canguraje}
                onChange={handleChange}
                name="canguraje"
              />
            }
            label="Canguraje"
          />
          <FormControlLabel
            control={
              <Checkbox
                checked={baño_mixto}
                onChange={handleChange}
                name="Baño mixto"
              />
            }
            label="Baño mixto"
          />
          <FormControlLabel
            control={
              <Checkbox
                checked={accesible_ruedas}
                onChange={handleChange}
                name="accesible_ruedas"
              />
            }
            label="Accesible ruedas"
          />
          <FormControlLabel
            control={
              <Checkbox
                checked={espacio_infantil}
                onChange={handleChange}
                name="espacio_infantil"
              />
            }
            label="Espacio Infantil"
          />
        </FormGroup>
      </FormControl>
    </Box>
  );
}
