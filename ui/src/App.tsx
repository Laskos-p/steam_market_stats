import { Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Games from "./pages/Games";
import Items from "./pages/Items";

export default function App() {
  return (
    <div className="container mx-auto p-4">
      <Navbar />
      <div className="p-4">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/games" element={<Games />} />
          <Route path="/items" element={<Items />} />
        </Routes>
      </div>
    </div>
  );
}
