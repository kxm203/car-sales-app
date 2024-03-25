import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import "./index.css";
import App from "./components/App";
import ErrorPage from "./components/ErrorPage.js";
import MustangPage from "./components/MustangPage.js";
import NewMustangForm from "./components/NewMustangForm.js";

const router = BrowserRouter([
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
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(router);