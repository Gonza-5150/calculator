import React, { useState } from "react";
import axios from "axios";

function Calculator() {
  const [num1, setNum1] = useState("");
  const [num2, setNum2] = useState("");
  const [result, setResult] = useState("");

  const handleAddition = async () => {
    const response = await axios.post("/addition", {
      num1: num1,
      num2: num2,
    });
    setResult(response.data.result);
  };

  return (
    <div>
      <h2>Calculator</h2>
      <form>
        <input
          type="number"
          placeholder="Enter number 1"
          value={num1}
          onChange={(e) => setNum1(e.target.value)}
        />
        <input
          type="number"
          placeholder="Enter number 2"
          value={num2}
          onChange={(e) => setNum2(e.target.value)}
        />
        <button type="button" onClick={handleAddition}>
          Add
        </button>
      </form>
      <p>Result: {result}</p>
    </div>
  );
}

export default Calculator;
