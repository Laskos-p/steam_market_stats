import { Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Games from "./pages/Games";
import Items from "./pages/Items";

export default function App() {
  return (
    <>
      <Navbar />
      <div className="bg-[#161920] py-4 text-center">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/games" element={<Games />} />
          <Route path="/items" element={<Items />} />
        </Routes>
      </div>
    </>
  );
}
