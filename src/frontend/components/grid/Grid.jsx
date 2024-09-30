import React, { useState, useRef } from "react";
import styles from "./Grid.module.css";

export const Grid = ({ onSubmit, highlightedPositions, onClear }) => {
  const [grid, setGrid] = useState(Array(16).fill(""));
  const [error, setError] = useState("");
  const inputRefs = useRef([]);

  const handleChange = (index, value) => {
    const newGrid = [...grid];
    newGrid[index] = value.toLowerCase();
    setGrid(newGrid);
    if (value && index < 15) {
      inputRefs.current[index + 1].focus();
    }
  };

  const handleClear = () => {
    setGrid(Array(16).fill(""));
    setError("");
    onClear();
    inputRefs.current[0].focus();
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    if (grid.includes("")) {
      setError("Please fill all 16 boxes with letters");
      return;
    }
    setError("");
    const letters = grid.join("");
    onSubmit(letters);
  };

  return (
    <form onSubmit={handleSubmit} className={styles.form}>
      <div className={styles.container}>
        {grid.map((letter, index) => {
          const isFirst = highlightedPositions[0] === index;
          return (
            <input
              key={index}
              type="text"
              maxLength="1"
              value={letter}
              ref={(el) => (inputRefs.current[index] = el)}
              onChange={(e) => handleChange(index, e.target.value)}
              className={`${styles.input} ${
                highlightedPositions.includes(index)
                  ? isFirst
                    ? styles.startHighlighted
                    : styles.highlighted
                  : ""
              }`}
            />
          );
        })}
      </div>
      {error && <p className={styles.error}>{error}</p>}
      <div className={styles.buttons}>
        <button type="submit" className={styles.submit}>
          Solve
        </button>
        <button type="button" className={styles.clear} onClick={handleClear}>
          Clear
        </button>
      </div>
    </form>
  );
};
