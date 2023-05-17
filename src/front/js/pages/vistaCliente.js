import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/cliente.css";

export const VistaCliente = () => {
  const { store, actions } = useContext(Context);

  return (
    <>
      <h3 className="text-success m-2 p-4">¡Welcome to calculator!</h3>
      <div className="m-2 p-3">
        <div className="d-flex justify-content-between align-middle">
          <div className="ms-5">
            <h4 className="text-success text-sm-start m-2">Calculator</h4>
            <div class="mb-3">
              <label for="formGroupExampleInput" class="form-label">
                First number
              </label>
              <input
                type="text"
                class="form-control"
                id="formGroupExampleInput"
                placeholder="Put your first number"
              />
            </div>
            <button type="button" class="btn btn-primary">
              +
            </button>
            <button type="button" class="btn btn-secondary">
              -
            </button>
            <button type="button" class="btn btn-success">
              X
            </button>
            <button type="button" class="btn btn-danger">
              %
            </button>
            <button type="button" class="btn btn-warning">
              sqr
            </button>
            <button type="button" class="btn btn-info">
              randN
            </button>
            <div class="mb-3">
              <label for="formGroupExampleInput2" class="form-label">
                Second number
              </label>
              <input
                type="text"
                class="form-control"
                id="formGroupExampleInput2"
                placeholder="Put your second number"
              />
            </div>
            <button type="button" class="btn btn-dark">
              Result
            </button>
            <input
              class="form-control"
              type="text"
              value="Result..."
              aria-label="result"
              readonly
            ></input>
          </div>
        </div>
      </div>
    </>
  );
};
