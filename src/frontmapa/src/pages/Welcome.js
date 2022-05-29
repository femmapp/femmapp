import { Link } from "react-router-dom";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";
import Image from "../assets/img/logo.png";

const sectionStyle = {
  height: "100vh",
  backgroundImage: `url(${Image})`,
  backgroundRepeat: "no-repeat",
  backgroundSize: "cover",
  opacity: "0.7",
};

export default function Welcome() {
  return (
    <>
      <Box style={sectionStyle}>
        <Container maxWidth="sm">
          <Typography
            component="h1"
            variant="h2"
            align="center"
            color="text.primary"
            marginTop={5}
            gutterBottom
          >
            CONSCIOUS MAP
          </Typography>
          <Typography
            variant="h5"
            align="center"
            color="text.secondary"
            paragraph
            marginTop={40}
          >
            Let's build a feminist inclusive map!
          </Typography>

          <Stack
            sx={{ pt: 4 }}
            direction="row"
            spacing={20}
            justifyContent="center"
          >
            <Button variant="contained" component={Link} to="/landing">
              Ir a mi mapa
            </Button>

            <Button variant="outlined" component={Link} to="/form">
              Unirme
            </Button>
          </Stack>
        </Container>
      </Box>
    </>
  );
}
