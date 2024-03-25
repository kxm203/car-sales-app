// import NavBar from "./NavBar";
import { useLocation } from "react-router-dom";

function ErrorPage() {
    const location = useLocation();
    console.error("Error in route:", location.pathname);

    const imageUrl = "https://www.carscoops.com/wp-content/uploads/2024/03/TKTK-2024-Lowell-Crash-Ford-Mustang-768x432.jpg";
    

    return (
        <>
            <header>
                {/* <NavBar /> */}
            </header>
            <main style={{ textAlign: 'center' }}>
                <h1>Yikes! You selected something that wasn't available!</h1>
                <img src={imageUrl} alt = "crashed" style={{ display: 'block', margin: '0 auto'}} />
            </main>
        </>
    );
};

export default ErrorPage;