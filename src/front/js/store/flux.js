import Swal from "sweetalert2/dist/sweetalert2.js";
import "../../img/cat-error.png";

const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      message: null,
      token: null,
      entrar: null,
      demo: [
        {
          title: "FIRST",
          background: "white",
          initial: "white",
        },
        {
          title: "SECOND",
          background: "white",
          initial: "white",
        },
      ],
    },
    actions: {
      // Use getActions to call a function within a fuction
      exampleFunction: () => {
        getActions().changeColor(0, "green");
      },

      syncTokenFromSessionStore: () => {
        const token = sessionStorage.getItem("token");
        console.log("Aplication loaded, synching the session storage token");
        if (token && token != "" && token != undefined)
          setStore({ token: token });

      },

      logout: () => {
        sessionStorage.removeItem("token");
        console.log("Login out");
        setStore({ token: null });
      },

      login: async (email, password) => {
        const opts = {
          method: "POST",
          headers: {
            "Content-type": "application/json",
          },
          body: JSON.stringify({
            email: email,
            password: password,
          }),
        };
        try {
          const resp = await fetch(
            process.env.BACKEND_URL + "/api/token",
            opts
          );
          if (resp.status !== 200) {
            if (resp.status === 401) {
              Swal.fire({
                imageUrl: "cat-error.png",
                imageWidth: 180,
                imageHeight: 180,
                imageAlt: "cat",
                title: "Ups",
                text: "Correo o contraseña incorrecta",
                confirmButtonColor: "orange"
              });
              return false;
            }
            Swal.fire({
              imageUrl: "cat-error.png",
              imageWidth: 180,
              imageHeight: 180,
              imageAlt: "cat",
              title: "Ups",
              text: "Error al accesar. Intente de nuevo.",
              confirmButtonColor: "orange"
            });
            return false;
          }

          const data = await resp.json();
          console.log("from the back", data);
          sessionStorage.setItem("token", data.access_token);
          console.log(data);
          setStore({ token: data.access_token });
          return true;
        } catch (error) {
          console.error("There has been an error");
        }
      },

      getMessage: () => {
        const store = getStore();
        const opts = {
          headers: {
            Authorization: "Bearer" + store.token,
          },
        };

        // fetching data from the backend
        fetch(process.env.BACKEND_URL + "/api/hello", opts)
          .then((resp) => resp.json())
          .then((data) => setStore({ message: data.message }))
          .catch((error) =>
            console.log("Error loading message from backend", error)
          );
      },
      changeColor: (index, color) => {
        //get the store
        const store = getStore();

        //we have to loop the entire demo array to look for the respective index
        //and change its color
        const demo = store.demo.map((elm, i) => {
          if (i === index) elm.background = color;
          return elm;
        });

        //reset the global store
        setStore({ demo: demo });
      },
    },
  };
};

export default getState;
