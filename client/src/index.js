import React from "react";
import ReactDOM from "react-dom/client";
import  { RouterProvider, createBrowserRouter } from  "react-router-dom"
import "./index.css";
import App from "./components/App";
import ErrorPage from "./components/ErrorPage.js";
import MustangPage from "./components/MustangPage.js";
import NewMustangForm from "./components/NewMustangForm.js";

const routes = [
    {
        path: "/",
        element: <App />
    },
    {
        path: "/Mustangs",
        element: <MustangPage />
    },
    {
        path: "/AddMustang",
        element: <NewMustangForm />
    },
    {
        path: "*",
        element: <ErrorPage />,
    }
];

const router = createBrowserRouter(routes)

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);