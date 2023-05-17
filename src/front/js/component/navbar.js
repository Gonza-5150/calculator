import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";
import "../../styles/navbar.css";
import "../../img/LogotipoPS.png";
import "../../img/navbar2.png";
import "../../img/dogs.png";
import "../../img/calculadora.png";

export const Navbar = () => {
  const { store, actions } = useContext(Context);
  const userLogueado = sessionStorage.getItem("token");
  const tipoUser = sessionStorage.getItem("tipoUsuario");

  return (
    <nav className="navbar navbar-expand-sm bg-light " id="navigation">
      <div className="container-fluid">
        <a className="navbar-brand ms-5 ps-2">
          <img
            src="calculadora.png"
            alt="Logo"
            width="100"
            height="100"
            className="d-inline-block align-text-top"
          />
        </a>
        <div>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="#navbarNav">
            <ul className="navbar-nav p-5">
              {!userLogueado && !tipoUser && (
                <>
                  <li
                    className="nav-item border border-white rounded mx-3 border-opacity-75 shadow-lg"
                    id="botonNav"
                  >
                    <a className="nav-link px-4" href="#bgBeneficios">
                      Beneficios
                    </a>
                  </li>
                  <li
                    className="nav-item border border-white rounded mx-3 border-opacity-75"
                    id="botonNav"
                  >
                    <a className="nav-link px-4" href="#aboutUs">
                      Nosotros
                    </a>
                  </li>
                  <li
                    className="nav-item border border-white rounded mx-3 border-opacity-75"
                    id="botonNav"
                  >
                    <a className="nav-link px-4" href="#contactUs">
                      Contacto
                    </a>
                  </li>
                </>
              )}
              {userLogueado && store.tipoUsuario == 1 && (
                <>
                  <Link to="/agenda">
                    <li
                      className="nav-item border border-white rounded mx-3 border-opacity-75"
                      id="botonNav"
                    >
                      <a className="nav-link px-4">Agenda</a>
                    </li>
                  </Link>
                  <Link to="/usuarios">
                    <li
                      className="nav-item border border-white rounded mx-3 border-opacity-75"
                      id="botonNav"
                    >
                      <a className="nav-link px-4">Usuarios</a>
                    </li>
                  </Link>
                  <Link to="/mascotas">
                    <li
                      className="nav-item border border-white rounded mx-3 border-opacity-75"
                      id="botonNav"
                    >
                      <a className="nav-link px-4">Mascotas</a>
                    </li>
                  </Link>
                  <Link to="/atencionmedica">
                    <li
                      className="nav-item border border-white rounded mx-3 border-opacity-75"
                      id="botonNav"
                    >
                      <a className="nav-link px-4">Atención Médica</a>
                    </li>
                  </Link>
                  <Link to="/">
                    <li
                      className="nav-item border border-white rounded mx-3 border-opacity-75"
                      id="botonNav"
                    >
                      <a
                        className="nav-link px-4"
                        onClick={() => actions.logout()}
                      >
                        Salir
                      </a>
                    </li>
                  </Link>
                </>
              )}
              {userLogueado && store.tipoUsuario == 2 && (
                <>
                  <Link to="/cliente">
                    <li
                      className="nav-item border border-white rounded mx-3 border-opacity-75"
                      id="botonNav"
                    >
                      <a className="nav-link px-4">Mis mascotas</a>
                    </li>
                  </Link>
                  <Link to="/editarperfil">
                    <li
                      className="nav-item border border-white rounded mx-3 border-opacity-75"
                      id="botonNav"
                    >
                      <a className="nav-link px-4">Mi perfil</a>
                    </li>
                  </Link>
                  <Link to="/">
                    <li
                      className="nav-item border border-white rounded mx-3 border-opacity-75"
                      id="botonNav"
                    >
                      <a
                        className="nav-link px-4"
                        onClick={() => actions.logout()}
                      >
                        Salir
                      </a>
                    </li>
                  </Link>
                </>
              )}
            </ul>
          </div>
        </div>
      </div>
    </nav>
  );
};
