import React, { useContext, useState } from "react";
import axios from "axios";
import { Context } from "../store/appContext";
import "../../styles/cliente.css";
import Calculator from "../component/calculator";

export const VistaCliente = () => {
  const { store, actions } = useContext(Context);

  const [operation, setOperation] = useState();
  const [firstNumber, setFirstNumber] = useState();
  const [secondNumber, setSecondNumber] = useState();

  return (
    <>
      <h3 className="text-success m-2 p-4">¡Welcome to calculator!</h3>
      <div className="m-2 p-3">
        <div className="d-flex justify-content-between align-middle">
          <div className="ms-5">
            <h4 className="text-success text-sm-start m-2">Calculator</h4>
            <div className="mb-3">
              <label htmlFor="formGroupExampleInput" className="form-label">
                First number
              </label>
              <input
                value={firstNumber}
                type="number"
                className="form-control"
                id="formGroupExampleInput"
                placeholder="Put your first number"
                onChange={(e) => setFirstNumber(Number(e.target.value))}
              />
              <button
                type="button"
                className="btn btn-warning"
                onClick={() => setOperation("sqrt")}
              >
                sqr
              </button>
              <div className="mb-3">
                <label htmlFor="formGroupExampleInput2" className="form-label">
                  Second number
                </label>
                <input
                  value={secondNumber}
                  type="number"
                  className="form-control"
                  id="formGroupExampleInput2"
                  placeholder="Put your second number"
                  onChange={(e) => setSecondNumber(Number(e.target.value))}
                />
              </div>
            </div>
            <button
              type="button"
              className="btn btn-primary"
              onClick={() => setOperation("addition")}
            >
              +
            </button>
            <button
              type="button"
              className="btn btn-secondary"
              onClick={() => setOperation("substraction")}
            >
              -
            </button>
            <button
              type="button"
              className="btn btn-success"
              onClick={() => setOperation("multiplication")}
            >
              X
            </button>
            <button
              type="button"
              className="btn btn-danger"
              onClick={() => setOperation("division")}
            >
              %
            </button>
            <button
              type="button"
              className="btn btn-info"
              onClick={() => setOperation("randn")}
            >
              randN
            </button>
            <input
              className="form-control"
              type="text"
              value="Result..."
              aria-label="result"
              readOnly
            ></input>
          </div>
        </div>
      </div>
    </>
  );
};
