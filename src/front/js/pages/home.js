import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="text-center mt-5">
			<h1>Hello Rigo!!</h1>
			<h1>Hello Rigo!!</h1>
			<h1>Hello Rigo!!</h1>
			<h1>Hello Rigo!!</h1>
			<h1>Hello Rigo!!</h1>
			<h1>Hello Rigo!!</h1>
			<h1>Hello Rigo!!</h1>
			<h1>Hello Rigo!!</h1>
			<h1>Hello Rigo!!</h1>
			<h1>Hello Rigo!!</h1>
			<p>
				
			</p>
			<div className="alert alert-info">
				{store.message || "Loading message from the backend (make sure your python backend is running)..."}
			</div>
			
		</div>
	);
};
