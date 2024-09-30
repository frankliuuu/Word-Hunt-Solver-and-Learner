import { useState } from "react";
import { Grid } from "./components/grid/Grid";
import { Solutions } from "./components/solutions/Solutions";
import styles from "./App.module.css";

function App() {
  const [solutions, setSolutions] = useState([]);
  const [highlightedPositions, setHighlightedPositions] = useState([]);

  const handleGridSubmit = async (letters) => {
    try {
      const response = await fetch("/api/find", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ board: letters }),
      });

      const result = await response.json();
      setSolutions(result);
    } catch (error) {
      console.error("Error solving:", error);
    }
  };

  const handleClear = () => {
    setSolutions({});
    setHighlightedPositions([]);
  };

  return (
    <div className={styles.app}>
      <div className={styles.grid}>
        <Grid
          onSubmit={handleGridSubmit}
          highlightedPositions={highlightedPositions}
          onClear={handleClear}
        />
      </div>
      <div className={styles.solutions}>
        <Solutions
          solutions={solutions}
          setHighlightedPositions={setHighlightedPositions}
        />
      </div>
    </div>
  );
}

export default App;
