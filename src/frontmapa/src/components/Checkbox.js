import * as React from "react";
import Box from "@mui/material/Box";
import FormLabel from "@mui/material/FormLabel";
import FormControl from "@mui/material/FormControl";
import FormGroup from "@mui/material/FormGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import FormHelperText from "@mui/material/FormHelperText";
import Checkbox from "@mui/material/Checkbox";

export default function CheckboxesGroup() {
  const [state, setState] = React.useState({
    cambiador: true,
    zona_lactancia: false,
    espacio_infantil: false,
    canguraje: true,
    accesible_ruedas: true,
    baño_mixto: false,
    baño_lavamanos: true,
    LGTBQ_friendy: true,
    ginecologia: true,
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
  const error =
    [
      cambiador,
      zona_lactancia,
      espacio_infantil,
      canguraje,
      accesible_ruedas,
      baño_mixto,
    ].filter((v) => v).length !== 2;

  return (
    <Box sx={{ display: "flex" }}>
      <FormControl sx={{ m: 3 }} component="fieldset" variant="standard">
        <FormLabel component="legend">Categorias</FormLabel>
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
        </FormGroup>
        <FormHelperText>Be careful</FormHelperText>
      </FormControl>
      <FormControl
        required
        error={error}
        component="fieldset"
        sx={{ m: 3 }}
        variant="standard"
      >
        <FormLabel component="legend">Pick two</FormLabel>
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
        </FormGroup>
        <FormHelperText>You can display an error</FormHelperText>
      </FormControl>
    </Box>
  );
}
