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
        element: <App />,
        errorElement: <ErrorPage />
    },
    {
        path: "/Mustangs",
        element: <MustangPage />,
        errorElement: <ErrorPage />
    },
    {
        path: "/AddMustang",
        element: <NewMustangForm />,
        errorElement: <ErrorPage />
    }
];

const router = createBrowserRouter(routes)

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);