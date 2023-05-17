import React, { Component } from "react";
import "../../styles/home.css";

export const Footer = () => (
  <>
    {/* Footer */}
    <footer
      className="text-center text-lg-start text-white mt-3"
      id="footer-container"
    >
      {/* Section: Social media */}
      {/* Section: Links  */}
      <section className="w-100">
        <div className="container-fluid text-center text-md-start mt-5 pt-1">
          {/* Grid row */}
          <div className="row mt-5">
            {/* Grid column */}
            <div className="col-md-3 col-lg-4 col-xl-1 mx-auto mb-3">
              {/* Content */}
              <img
                src="calculadora.png"
                alt="Logo"
                width="75"
                height="75"
                className="align-middle"
              />
            </div>
            {/* Grid column */}
            {/* Grid column */}
            <div className="col-md-2 col-lg-2 col-xl-2 mx-auto mb-2">
              {/* Links */}
              <h6 className="text-uppercase fw-bold mb-3">Servicios</h6>
              <p></p>
              <p></p>
              <p></p>
              <p>
                <a className="text-reset" href="#contactUs">
                  Contáctenos
                </a>
              </p>
            </div>
            <div className="col-md-1 col-lg-1 col-xl-3 mx-auto mb-md-0 mb-1">
              {/* Links */}
              <h6 className="text-uppercase fw-bold mb-3">Contactenos</h6>

              <p>
                <i className="fas fa-envelope me-2" />
                estevesgonzalo@hotmail.com
              </p>
              <p>
                <i className="fas fa-phone me-2" /> +54 11 3469 4414
              </p>
            </div>
            {/* Grid column */}
          </div>
          {/* Grid row */}
        </div>
      </section>

      {/* Copyright */}
      <div className="text-center p-1" style={{ backgroundColor: "white" }}>
        {" "}
        2022 <a className="text-reset fw-bold">© Petsource</a>
      </div>
      {/* Copyright */}
    </footer>
    {/* Footer */}
  </>
);
