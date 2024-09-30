import React, { useState } from "react";
import styles from "./solutions.module.css";

export const Solutions = ({ solutions, setHighlightedPositions }) => {
  const [hoveredWord, setHoveredWord] = useState(null);

  const handleMouseEnter = (positions, word, definition) => {
    setHighlightedPositions(positions);
    setHoveredWord({ word, definition });
  };

  const handleMouseLeave = () => {
    setHighlightedPositions([]);
    setHoveredWord(null);
  };

  const renderSolutions = () => {
    const wordEntries = [];

    for (let length in solutions) {
      const words = solutions[length];
      for (let word in words) {
        const { positions, definition } = words[word];

        wordEntries.push(
          <div
            key={word}
            onMouseEnter={() => handleMouseEnter(positions, word, definition)}
            onMouseLeave={handleMouseLeave}
            className={styles.item}
          >
            <strong>{word}</strong> <br /> (Length: {length})
          </div>
        );
      }
    }

    if (wordEntries.length === 0) {
      return <p>No words found.</p>;
    }
    wordEntries.reverse();
    return <div className={styles.grid}>{wordEntries}</div>;
  };

  return (
    <div className={styles.container}>
      <div className={styles.list}>
        <h3>Words Found:</h3>
        {renderSolutions()}
      </div>
      <div className={styles.definition}>
        {hoveredWord ? (
          <div>
            <strong>{hoveredWord.word}</strong>: {hoveredWord.definition}
          </div>
        ) : (
          <p>Hover over a word to see the definition</p>
        )}
      </div>
    </div>
  );
};
