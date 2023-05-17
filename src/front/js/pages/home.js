import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import { Login } from "../component/login";

export const Home = () => {
  const { store, actions } = useContext(Context);

  return (
    <div>
      <Login />
    </div>
  );
};
