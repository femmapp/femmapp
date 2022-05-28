import Navbar from "../components/Navbar";
import styles from "./Landing.module.css";

function Landing() {
  return (
    <>
      <Navbar />
      <div id="map"></div>
      <div className={styles.mapbox}>
        <div id="map"></div>
      </div>
    </>
  );
}

export default Landing;
